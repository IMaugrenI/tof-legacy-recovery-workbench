from __future__ import annotations

import asyncio
from pathlib import Path

from .io_utils import read_json, write_json
from .models import EvidenceRecord, HypothesisBundle, SplitExtract


async def run_extractors(repo_root: Path) -> list[SplitExtract]:
    evidence_root = repo_root / '02_evidence'
    hypotheses_root = repo_root / '03_hypotheses'
    output_root = repo_root / '04_extracts'
    paths = [path for path in evidence_root.glob('*.json') if (hypotheses_root / path.name).exists()]
    tasks = [asyncio.to_thread(build_extract, evidence_path, hypotheses_root / evidence_path.name, output_root) for evidence_path in paths]
    return await asyncio.gather(*tasks)


def build_extract(evidence_path: Path, hypothesis_path: Path, output_root: Path) -> SplitExtract:
    evidence = EvidenceRecord(**read_json(evidence_path))
    bundle_raw = read_json(hypothesis_path)
    bundle = HypothesisBundle(
        source_id=bundle_raw['source_id'],
        rel_path=bundle_raw['rel_path'],
        hypotheses=[],
        review_flags=bundle_raw['review_flags'],
        unknown_patterns=bundle_raw['unknown_patterns'],
    )
    terms = set(evidence.text_terms)
    discord = {
        'detected': any(item.family == 'discord' for item in bundle.hypotheses) or 'discord_channel_like' in evidence.structural_markers,
        'channels': sorted({term for term in terms if term.startswith('#') or term in {'channel', 'general', 'rules'}}),
        'roles': sorted({term for term in terms if term in {'role', 'admin', 'moderator'}}),
        'permissions': sorted({term for term in terms if term in {'permission', 'manage_messages', 'ban_members'}}),
        'source_refs': evidence.source_refs,
    }
    bot = {
        'detected': 'bot_command_like' in evidence.structural_markers or any(term in terms for term in {'ctx', 'interaction', 'command'}),
        'commands': sorted({term for term in terms if term in {'command', 'slash', 'hybrid_command', 'ban', 'ctx', 'interaction'}}),
        'modules': sorted({ident for ident in evidence.technical_identifiers if '.' in ident})[:40],
        'touchpoints': sorted({term for term in terms if term in {'redis', 'postgres', 'api', 'queue'}}),
        'source_refs': evidence.source_refs,
    }
    repo = {
        'detected': 'repo_compose_like' in evidence.structural_markers or any(term in terms for term in {'services', 'postgres', 'redis', 'docker'}),
        'services': sorted({term for term in terms if term in {'services', 'bot', 'postgres', 'redis'}}),
        'infra_markers': list(evidence.structural_markers),
        'db_touchpoints': sorted({term for term in terms if term in {'postgres', 'redis', 'sqlalchemy', 'migration'}}),
        'source_refs': evidence.source_refs,
    }
    conflict = {
        'split_required': sum(1 for item in [discord, bot, repo] if item['detected']) > 1,
        'ambiguity_flags': evidence.ambiguity_flags,
        'review_flags': bundle.review_flags,
        'unknown_patterns': evidence.unknown_patterns,
    }
    extract = SplitExtract(
        source_id=evidence.source_id,
        rel_path=evidence.rel_path,
        discord_topology=discord,
        bot_surface=bot,
        repo_runtime=repo,
        conflict_report=conflict,
    )
    write_json(output_root / f'{evidence.source_id}.json', extract.to_dict())
    return extract
