#!/usr/bin/env python3
"""Verify the frozen package manifest, excluding ignored build/cache/Git files."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent.parent
manifest=ROOT/'SHA256SUMS';assert manifest.exists(),'SHA256SUMS is missing'
count=0
for line in manifest.read_text().splitlines():
 digest,name=line.split('  ',1);path=ROOT/name
 assert path.is_file(),('missing file',name)
 assert hashlib.sha256(path.read_bytes()).hexdigest()==digest,('checksum mismatch',name)
 count+=1
print('Verified',count,'SHA256 checksums.')
