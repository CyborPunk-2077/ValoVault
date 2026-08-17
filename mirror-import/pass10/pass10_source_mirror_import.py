#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, hashlib, json, lzma, shutil, subprocess, tarfile
from pathlib import Path


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def check(path: Path, size: int, digest: str, label: str):
    if path.stat().st_size != size:
        raise SystemExit(f'{label} size mismatch: {path.stat().st_size} != {size}')
    got = sha(path)
    if got != digest:
        raise SystemExit(f'{label} sha mismatch: {got} != {digest}')


def concat_parts(repo: Path, cfg: dict, out: Path):
    parts = []
    for i in range(cfg['partCount']):
        p = repo / cfg['partsDir'] / f'part-{i:03d}.b64'
        if not p.is_file():
            raise SystemExit(f'missing part {p}')
        parts.append(p.read_bytes())
    out.write_bytes(b''.join(parts))
    check(out, cfg['base64Size'], cfg['base64Sha256'], out.name)


def run(cmd, cwd=None):
    print('+', ' '.join(map(str, cmd)), flush=True)
    subprocess.run(cmd, cwd=cwd, check=True)


def audit_tree(root: Path, expected_json: Path):
    exp = json.loads(expected_json.read_text('utf-8'))
    expected = {x['path']: (x['size'], x['sha256']) for x in exp['files']}
    actual = {}
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.parts:
            continue
        rel = p.relative_to(root).as_posix()
        actual[rel] = (p.stat().st_size, sha(p))
    missing = sorted(set(expected) - set(actual))
    extra = sorted(set(actual) - set(expected))
    bad = sorted(k for k in expected.keys() & actual.keys() if expected[k] != actual[k])
    result = {'expected': len(expected), 'actual': len(actual), 'missing': missing, 'extra': extra, 'hashOrSizeMismatch': bad}
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in result.items()}, indent=2))
    if missing or extra or bad:
        if missing:
            print('missing:', missing[:20])
        if extra:
            print('extra:', extra[:20])
        if bad:
            print('bad:', bad[:20])
        raise SystemExit('final source audit failed')
    return exp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--result', required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    work = Path(args.work).resolve()
    result = Path(args.result).resolve()
    cfg = json.loads((repo / 'mirror-import/pass10/import-manifest.json').read_text('utf-8'))
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    payload = work / 'delta.b64'
    concat_parts(repo, cfg['delta'], payload)
    xz = work / 'delta.patch.xz'
    xz.write_bytes(base64.b64decode(payload.read_bytes(), validate=True))
    check(xz, cfg['delta']['xzSize'], cfg['delta']['xzSha256'], 'delta xz')
    patch = work / 'delta.patch'
    patch.write_bytes(lzma.decompress(xz.read_bytes()))
    check(patch, cfg['delta']['patchSize'], cfg['delta']['patchSha256'], 'delta patch')

    mb64 = work / 'expected.b64'
    concat_parts(repo, cfg['expectedManifest'], mb64)
    mxz = work / 'expected.json.xz'
    mxz.write_bytes(base64.b64decode(mb64.read_bytes(), validate=True))
    check(mxz, cfg['expectedManifest']['xzSize'], cfg['expectedManifest']['xzSha256'], 'manifest xz')
    mjson = work / 'expected.json'
    mjson.write_bytes(lzma.decompress(mxz.read_bytes()))
    check(mjson, cfg['expectedManifest']['jsonSize'], cfg['expectedManifest']['jsonSha256'], 'manifest json')
    expected = json.loads(mjson.read_text('utf-8'))
    if expected.get('intendedTrackedCount') != cfg['intendedTrackedCount'] or len(expected.get('files', [])) != cfg['intendedTrackedCount']:
        raise SystemExit('expected manifest count mismatch')

    archive = repo / cfg['baseSourceArchive']
    if not archive.is_file():
        raise SystemExit(f'missing base source archive: {archive}')
    extract = work / 'base-extract'
    extract.mkdir()
    with tarfile.open(archive, 'r:xz') as tf:
        tf.extractall(extract)
    roots = [p.parent for p in extract.rglob('MASTER_BUILD_PROMPT.md')]
    if len(roots) != 1:
        raise SystemExit(f'expected one project root in base archive, found {len(roots)}')
    src = roots[0]
    tree = work / 'source'
    shutil.copytree(src, tree)
    shutil.rmtree(tree / 'docs/recovery/source-snapshots', ignore_errors=True)
    for rel in ('CHECKPOINT_MANIFEST.json', 'PACKAGE_CONTENT_MANIFEST.json'):
        (tree / rel).unlink(missing_ok=True)

    run(['git', 'init', '-q'], cwd=tree)
    run(['git', 'clean', '-fdX', '-q'], cwd=tree)
    run(['git', 'config', 'user.name', 'ValoVault Mirror Import'], cwd=tree)
    run(['git', 'config', 'user.email', 'valovault-mirror@users.noreply.github.com'], cwd=tree)
    run(['git', 'add', '-A'], cwd=tree)
    run(['git', 'commit', '-qm', 'filtered Pass 01 base'], cwd=tree)
    run(['git', 'apply', '--binary', '--check', str(patch)], cwd=tree)
    run(['git', 'apply', '--binary', str(patch)], cwd=tree)
    audit_tree(tree, mjson)
    shutil.rmtree(tree / '.git')

    out = {
        'status': 'PASS',
        'sourceRoot': str(tree),
        'expectedManifest': str(mjson),
        'intendedTrackedCount': cfg['intendedTrackedCount'],
        'canonicalPass10ZipSha256': cfg['canonicalPass10ZipSha256'],
        'classificationManifestSha256': cfg['classificationManifestSha256'],
        'deltaBase64Sha256': cfg['delta']['base64Sha256'],
        'expectedManifestSha256': cfg['expectedManifest']['jsonSha256']
    }
    result.write_text(json.dumps(out, indent=2) + '\n', 'utf-8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
