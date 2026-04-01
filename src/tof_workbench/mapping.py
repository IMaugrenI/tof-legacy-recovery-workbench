from __future__ import annotations

import asyncio
from pathlib import Path

from .io_utils import read_json, write_json
from .models import MappingRecord, SplitExtract
from .pathing import sanitize_rel_path

TARGET_CLASSES = {'discord', 'bot', 'repo', 'review_required'}


async def run_mapping(repo_root: Path) -> list[MappingRecord]:
    extract_root = repo_root / '04_extracts'
    output_root = repo_root / '05_mapping'
    review_root = repo_root / '06_review'
    paths = list(extract_root.glob('*.json'))
    tasks = [asyncio.to_thread(build_mapping, path, output_root, review_root) for path in paths]
    records = await asyncio.gather(*tasks)
    write_json(output_root / 'mapping_suggestions.json', {'records': [record.to_dict() for record in records]})
    return records


def build_mapping(extract_path: Path, output_root: Path, review_root: Path) -> MappingRecord:
    split = SplitExtract(**read_json(extract_path))
    target_classes: list[str] = []
    target_paths: dict[str, str] = {}
    rationale: dict[str, dict] = {}

    if split.discord_topology.get('detected'):
        target_classes.append('discord')
        target_paths['discord'] = f"discord/{sanitize_rel_path(split.rel_path)}__discord_topology.json"
        rationale['discord'] = {'channels': len(split.discord_topology.get('channels', [])), 'roles': len(split.discord_topology.get('roles', []))}
    if split.bot_surface.get('detected'):
        target_classes.append('bot')
        target_paths['bot'] = f"bot/{sanitize_rel_path(split.rel_path)}__bot_surface.json"
        rationale['bot'] = {'commands': len(split.bot_surface.get('commands', [])), 'modules': len(split.bot_surface.get('modules', []))}
    if split.repo_runtime.get('detected'):
        target_classes.append('repo')
        target_paths['repo'] = f"repo/{sanitize_rel_path(split.rel_path)}__repo_runtime.json"
        rationale['repo'] = {'services': len(split.repo_runtime.get('services', [])), 'db_touchpoints': len(split.repo_runtime.get('db_touchpoints', []))}

    review_required = False
    if split.conflict_report.get('split_required') or split.conflict_report.get('unknown_patterns'):
        review_required = True
        if 'review_required' not in target_classes:
            target_classes.append('review_required')
            target_paths['review_required'] = f"review_required/{sanitize_rel_path(split.rel_path)}__review.json"
            rationale['review_required'] = {
                'ambiguity_flags': split.conflict_report.get('ambiguity_flags', []),
                'review_flags': split.conflict_report.get('review_flags', []),
                'unknown_patterns': split.conflict_report.get('unknown_patterns', []),
            }

    if not target_classes:
        review_required = True
        target_classes = ['review_required']
        target_paths = {'review_required': f"review_required/{sanitize_rel_path(split.rel_path)}__review.json"}
        rationale = {'review_required': {'reason': 'no_target_detected'}}

    record = MappingRecord(
        source_id=split.source_id,
        rel_path=split.rel_path,
        target_classes=target_classes,
        target_paths=target_paths,
        rationale=rationale,
        review_required=review_required,
    )
    write_json(output_root / f'{split.source_id}.json', record.to_dict())
    if review_required:
        write_json(review_root / f'{split.source_id}.json', record.to_dict())
    return record
