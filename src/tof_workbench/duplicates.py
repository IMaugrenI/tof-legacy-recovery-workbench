from __future__ import annotations

import difflib
import hashlib
from pathlib import Path

from .io_utils import read_json, write_json


def run_duplicates(repo_root: Path) -> dict:
    intake_root = repo_root / '01_intake'
    output_path = repo_root / '07_reports' / 'duplicates.json'
    items = [read_json(path) for path in intake_root.glob('*.json')]
    exact_map: dict[str, list[str]] = {}
    snippets: list[tuple[str, str]] = []
    for item in items:
        payload = (item.get('text_excerpt', '') + '\n' + '\n'.join(item.get('strings_excerpt', []))).encode('utf-8', errors='ignore')
        digest = hashlib.sha256(payload).hexdigest()
        exact_map.setdefault(digest, []).append(item['rel_path'])
        snippets.append((item['rel_path'], (item.get('text_excerpt', '') or '\n'.join(item.get('strings_excerpt', [])))[:1200]))
    exact_duplicates = [paths for paths in exact_map.values() if len(paths) > 1]
    near_duplicates = []
    for idx, (path_a, sample_a) in enumerate(snippets[:200]):
        for path_b, sample_b in snippets[idx + 1:200]:
            if not sample_a or not sample_b:
                continue
            ratio = difflib.SequenceMatcher(a=sample_a, b=sample_b).ratio()
            if ratio >= 0.92:
                near_duplicates.append({'a': path_a, 'b': path_b, 'ratio': round(ratio, 3)})
    payload = {'exact_duplicates': exact_duplicates, 'near_duplicates': near_duplicates[:200]}
    write_json(output_path, payload)
    return payload
