from __future__ import annotations

from collections import Counter
from pathlib import Path

from .io_utils import read_json, write_json

TARGET_CLASSES = {'discord', 'bot', 'repo', 'review_required'}


def run_acceptance(repo_root: Path) -> dict:
    input_files = [path for path in (repo_root / '00_input_alt').rglob('*') if path.is_file()]
    intake_files = list((repo_root / '01_intake').glob('*.json'))
    mapping_files = [path for path in (repo_root / '05_mapping').glob('*.json') if path.name != 'mapping_suggestions.json']
    review_files = list((repo_root / '06_review').glob('*.json'))
    intake_data = [read_json(path) for path in intake_files]
    mapping_data = [read_json(path) for path in mapping_files]
    no_extension_total = sum(1 for path in input_files if not path.suffix)
    no_extension_processed = sum(1 for item in intake_data if not item.get('has_extension', False))
    modality_counts = Counter(item.get('detected_modality', 'unknown') for item in intake_data)
    target_counter = Counter()
    invalid_target_classes = []
    split_multi = 0
    for item in mapping_data:
        stable = 0
        for cls in item.get('target_classes', []):
            target_counter[cls] += 1
            if cls not in TARGET_CLASSES:
                invalid_target_classes.append({'rel_path': item.get('rel_path'), 'target_class': cls})
            if cls in {'discord', 'bot', 'repo'}:
                stable += 1
        if stable > 1:
            split_multi += 1
    payload = {
        'input_total_files': len(input_files),
        'intake_total_files': len(intake_files),
        'coverage_ratio': round(len(intake_files) / max(1, len(input_files)), 3),
        'no_extension_total': no_extension_total,
        'no_extension_processed': no_extension_processed,
        'no_extension_coverage_ratio': round(no_extension_processed / max(1, no_extension_total), 3),
        'detected_modalities': dict(modality_counts),
        'mapping_target_classes': dict(target_counter),
        'invalid_target_classes': invalid_target_classes,
        'review_total': len(review_files),
        'split_multi_target_count': split_multi,
        'default_run_materializes_code': False,
    }
    write_json(repo_root / '07_reports' / 'acceptance.json', payload)
    return payload
