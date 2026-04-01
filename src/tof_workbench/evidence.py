from __future__ import annotations

import asyncio
import re
from collections import Counter
from pathlib import Path

from .io_utils import read_json, write_json
from .models import EvidenceRecord, IntakeRecord

STOPWORDS = {'the', 'and', 'der', 'die', 'das', 'und', 'oder', 'mit', 'this', 'that', 'json', 'true', 'false'}
STRUCTURAL_GROUPS = {
    'discord_channel_like': ['channel', 'category', 'guild', '#general', '#rules'],
    'discord_role_like': ['role', 'permission', 'moderator', 'admin'],
    'bot_command_like': ['@commands.', 'hybrid_command', 'slash', 'ctx', 'interaction'],
    'repo_compose_like': ['services:', 'image:', 'depends_on:', 'volumes:', 'ports:'],
    'repo_db_like': ['postgres', 'redis', 'migration', 'sqlalchemy'],
}


async def run_evidence(repo_root: Path) -> list[EvidenceRecord]:
    intake_root = repo_root / '01_intake'
    output_root = repo_root / '02_evidence'
    paths = list(intake_root.glob('*.json'))
    tasks = [asyncio.to_thread(build_evidence, path, output_root) for path in paths]
    return await asyncio.gather(*tasks)


def build_evidence(intake_path: Path, output_root: Path) -> EvidenceRecord:
    intake = IntakeRecord(**read_json(intake_path))
    text = intake.text_excerpt or '\n'.join(intake.strings_excerpt)
    lowered = text.lower()
    terms = top_terms(lowered)
    technical_identifiers = sorted(set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_.]{2,}\b', text)))[:100]
    structural_markers = []
    for marker, hints in STRUCTURAL_GROUPS.items():
        if any(hint.lower() in lowered for hint in hints):
            structural_markers.append(marker)
    relation_hints = [hint for hint in ['depends_on', 'bridge', 'gateway', 'queue', 'worker'] if hint in lowered]
    ambiguity_flags = []
    if 'discord_channel_like' in structural_markers and 'repo_compose_like' in structural_markers:
        ambiguity_flags.append('discord_and_repo_overlap')
    if 'discord_role_like' in structural_markers and 'bot_command_like' in structural_markers:
        ambiguity_flags.append('discord_and_bot_overlap')
    unknown_patterns = [term for term, count in Counter(terms).items() if count >= 2 and term.startswith('x_')][:30]

    evidence = EvidenceRecord(
        source_id=intake.source_id,
        rel_path=intake.rel_path,
        detected_modality=intake.detected_modality,
        confidence=intake.confidence,
        text_terms=terms,
        technical_identifiers=technical_identifiers,
        structural_markers=structural_markers,
        relation_hints=relation_hints,
        path_hints=intake.path_hints,
        ambiguity_flags=ambiguity_flags,
        unknown_patterns=unknown_patterns,
        source_refs=[f'01_intake/{intake_path.name}'],
    )
    write_json(output_root / f'{intake.source_id}.json', evidence.to_dict())
    return evidence


def top_terms(text: str) -> list[str]:
    words = re.findall(r'\b[a-zA-Z_#][a-zA-Z0-9_#.-]{2,}\b', text)
    filtered = [word for word in words if word not in STOPWORDS]
    counts = Counter(filtered)
    return [term for term, _count in counts.most_common(120)]
