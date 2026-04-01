from __future__ import annotations

import asyncio
from pathlib import Path

from .io_utils import read_json, write_json
from .models import EvidenceRecord, HypothesisBundle, HypothesisRecord

WEIGHTS = {
    'discord': {'discord_channel_like': 0.5, 'discord_role_like': 0.35, 'guild': 0.2, 'channel': 0.2},
    'bot': {'bot_command_like': 0.5, 'command': 0.2, 'interaction': 0.2, 'ctx': 0.15},
    'repo': {'repo_compose_like': 0.5, 'repo_db_like': 0.35, 'docker': 0.2, 'postgres': 0.15, 'redis': 0.15},
}


async def run_hypotheses(repo_root: Path) -> list[HypothesisBundle]:
    evidence_root = repo_root / '02_evidence'
    output_root = repo_root / '03_hypotheses'
    paths = list(evidence_root.glob('*.json'))
    tasks = [asyncio.to_thread(build_bundle, path, output_root) for path in paths]
    bundles = await asyncio.gather(*tasks)
    write_json(output_root / 'unknown_cluster_suggestions.json', {
        'review_only': True,
        'suggestions': sorted({term for bundle in bundles for term in bundle.unknown_patterns})[:100],
    })
    return bundles


def build_bundle(evidence_path: Path, output_root: Path) -> HypothesisBundle:
    evidence = EvidenceRecord(**read_json(evidence_path))
    hypotheses: list[HypothesisRecord] = []
    for family, weights in WEIGHTS.items():
        score = 0.0
        for marker in evidence.structural_markers:
            score += weights.get(marker, 0.0)
        for term in evidence.text_terms[:40]:
            score += weights.get(term, 0.0)
        if score > 0:
            hypotheses.append(HypothesisRecord(family=family, confidence=round(min(score, 0.99), 3), evidence_refs=evidence.source_refs))
    hypotheses.sort(key=lambda item: item.confidence, reverse=True)
    review_flags = list(evidence.ambiguity_flags)
    if not hypotheses:
        review_flags.append('no_clear_family')
    bundle = HypothesisBundle(
        source_id=evidence.source_id,
        rel_path=evidence.rel_path,
        hypotheses=hypotheses,
        review_flags=review_flags,
        unknown_patterns=evidence.unknown_patterns,
    )
    write_json(output_root / f'{evidence.source_id}.json', bundle.to_dict())
    return bundle
