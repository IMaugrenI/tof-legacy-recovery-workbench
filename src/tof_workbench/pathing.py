from __future__ import annotations

import hashlib
import re
from pathlib import Path

_STAGE_DIRS = {
    "00_input_alt",
    "01_intake",
    "02_evidence",
    "03_hypotheses",
    "04_extracts",
    "05_mapping",
    "06_review",
    "07_reports",
    "docs",
    "src",
    "tests",
}

_slug_re = re.compile(r"[^a-zA-Z0-9._-]+")


def source_id_for_rel_path(rel_path: str) -> str:
    return hashlib.sha1(rel_path.encode("utf-8")).hexdigest()[:16]


def sanitize_rel_path(rel_path: str) -> str:
    cleaned = rel_path.replace("\\", "/").strip("/")
    return _slug_re.sub("_", cleaned)


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / "MANIFEST.md").exists() and (candidate / "00_input_alt").exists():
            return candidate
    raise FileNotFoundError("workbench root not found")
