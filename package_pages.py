"""Validate exact payload, then use the official uploader's GNU tar layout.
Keep approved dot metadata; add only container directory entries, never site files.
"""
from pathlib import Path
import sys,json,hashlib,tarfile,subprocess
root=Path(sys.argv[1]).resolve();dest=Path(sys.argv[2]).resolve();m=json.loads((root/'export-manifest.json').read_text());names={r['filename']for r in m['files']};allpaths=list(root.rglob('*'));actual={str(p.relative_to(root))for p in allpaths if p.is_file()}
assert not any(p.is_symlink()for p in allpaths),'No symlinks allowed'
assert actual==names|{'export-manifest.json'},'Unexpected export files'
for row in m['files']:
 p=root/row['filename'];assert p.resolve().is_relative_to(root);assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['filename']
# Same ./ root and explicit directory records as actions/upload-pages-artifact.
# Unlike its default exclusion, retain .vite files already expressly approved.
subprocess.run(['tar','--dereference','--hard-dereference','--format=gnu','--owner=0','--group=0','--directory',str(root),'-cf',str(dest),'.'],check=True)
with tarfile.open(dest)as archive:
 entries=archive.getmembers();assert entries[0].isdir()and entries[0].name=='.'
 files={e.name[2:]if e.name.startswith('./')else e.name:e for e in entries if e.isfile()};assert set(files)==actual
 assert not any(e.issym()or e.islnk()for e in entries)
 for name,entry in files.items():
  expected=hashlib.sha256((root/name).read_bytes()).hexdigest();assert hashlib.sha256(archive.extractfile(entry).read()).hexdigest()==expected,name
print('PASS exact official-layout Pages tar:',len(files),'regular files;',sum(e.isdir()for e in entries),'directory records; all file hashes unchanged, including approved dot metadata; no links')
