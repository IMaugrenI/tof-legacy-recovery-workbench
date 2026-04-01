from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class IntakeRecord:
    source_id: str
    rel_path: str
    size_bytes: int
    extension: str
    has_extension: bool
    detected_modality: str
    parser_used: str
    confidence: float
    is_binary: bool
    encoding: str | None
    mime_hint: str | None
    shebang: str | None
    path_hints: list[str] = field(default_factory=list)
    text_excerpt: str = ""
    strings_excerpt: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvidenceRecord:
    source_id: str
    rel_path: str
    detected_modality: str
    confidence: float
    text_terms: list[str]
    technical_identifiers: list[str]
    structural_markers: list[str]
    relation_hints: list[str]
    path_hints: list[str]
    ambiguity_flags: list[str]
    unknown_patterns: list[str]
    source_refs: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class HypothesisRecord:
    family: str
    confidence: float
    evidence_refs: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class HypothesisBundle:
    source_id: str
    rel_path: str
    hypotheses: list[HypothesisRecord]
    review_flags: list[str]
    unknown_patterns: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            'source_id': self.source_id,
            'rel_path': self.rel_path,
            'hypotheses': [item.to_dict() for item in self.hypotheses],
            'review_flags': self.review_flags,
            'unknown_patterns': self.unknown_patterns,
        }


@dataclass(slots=True)
class SplitExtract:
    source_id: str
    rel_path: str
    discord_topology: dict[str, Any]
    bot_surface: dict[str, Any]
    repo_runtime: dict[str, Any]
    conflict_report: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class MappingRecord:
    source_id: str
    rel_path: str
    target_classes: list[str]
    target_paths: dict[str, str]
    rationale: dict[str, Any]
    review_required: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


ROOT_MARKERS = {
    '00_input_alt',
    '01_intake',
    '02_evidence',
    '03_hypotheses',
    '04_extracts',
    '05_mapping',
    '06_review',
    '07_reports',
    'src',
    'docs',
}


def find_repo_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / 'MANIFEST.md').exists() and (candidate / '00_input_alt').exists():
            return candidate
    raise FileNotFoundError('workbench root not found')
