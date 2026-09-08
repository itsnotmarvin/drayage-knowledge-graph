"""Verify the fixed evidence copy without needing the original checkout."""

import hashlib
import json
from pathlib import Path


def verify(root):
    root = Path(root).resolve()
    manifest = json.loads((root / "evidence-snapshot.json").read_text())
    expected = manifest["files"]
    actual = {p.relative_to(root).as_posix() for p in (root / "data").rglob("*")
              if p.is_file() and p.name != ".DS_Store"}
    if actual != set(expected):
        raise ValueError(f"Evidence inventory changed: missing={sorted(set(expected) - actual)}, "
                         f"extra={sorted(actual - set(expected))}")
    for relative, digest in expected.items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root / "data"):
            raise ValueError(f"Evidence path escapes data/: {relative}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"Evidence checksum mismatch: {relative}")
    return len(expected)


if __name__ == "__main__":
    print(f"Verified {verify(Path(__file__).resolve().parents[1])} unchanged evidence files.")
