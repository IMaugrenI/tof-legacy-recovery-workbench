from __future__ import annotations

import asyncio
import mimetypes
import re
from pathlib import Path

from .io_utils import ensure_dir, safe_text_excerpt, write_json
from .models import IntakeRecord
from .pathing import sanitize_rel_path, source_id_for_rel_path

TEXT_EXTENSIONS = {'.txt', '.md', '.py', '.json', '.yml', '.yaml', '.ini', '.sh', '.html', '.cfg'}


async def run_intake(repo_root: Path) -> list[IntakeRecord]:
    input_root = repo_root / '00_input_alt'
    output_root = repo_root / '01_intake'
    ensure_dir(output_root)
    files = [p for p in input_root.rglob('*') if p.is_file()]
    tasks = [asyncio.to_thread(analyze_file, path, input_root, output_root) for path in files]
    return await asyncio.gather(*tasks)


def analyze_file(path: Path, input_root: Path, output_root: Path) -> IntakeRecord:
    rel_path = path.relative_to(input_root).as_posix()
    source_id = source_id_for_rel_path(rel_path)
    raw = path.read_bytes()
    extension = path.suffix.lower()
    has_extension = bool(extension)
    is_binary = looks_binary(raw)
    encoding = None
    text_excerpt = ''
    strings_excerpt: list[str] = []
    parser_used = 'binary_scan' if is_binary else 'text_decode'
    shebang = raw[:120].decode('utf-8', errors='ignore').splitlines()[0] if raw.startswith(b'#!') else None

    if not is_binary:
        decoded, encoding = decode_text(raw)
        text_excerpt = safe_text_excerpt(decoded)
        parser_used = choose_text_parser(extension, decoded, shebang)
    else:
        strings_excerpt = extract_strings(raw)
        if strings_excerpt:
            text_excerpt = safe_text_excerpt('\n'.join(strings_excerpt[:60]))

    mime_hint = mimetypes.guess_type(path.name)[0]
    detected_modality = determine_modality(extension, parser_used, text_excerpt, strings_excerpt)
    path_hints = path_hint_tokens(rel_path)
    confidence = 0.85 if parser_used != 'text_decode' else (0.7 if not is_binary else 0.6)

    record = IntakeRecord(
        source_id=source_id,
        rel_path=rel_path,
        size_bytes=len(raw),
        extension=extension,
        has_extension=has_extension,
        detected_modality=detected_modality,
        parser_used=parser_used,
        confidence=round(confidence, 3),
        is_binary=is_binary,
        encoding=encoding,
        mime_hint=mime_hint,
        shebang=shebang,
        path_hints=path_hints,
        text_excerpt=text_excerpt,
        strings_excerpt=strings_excerpt[:80],
    )
    write_json(output_root / f'{source_id}__{sanitize_rel_path(rel_path)}.json', record.to_dict())
    return record


def decode_text(raw: bytes) -> tuple[str, str | None]:
    for encoding in ('utf-8', 'latin-1'):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return raw.decode('utf-8', errors='replace'), 'utf-8-replace'


def looks_binary(raw: bytes) -> bool:
    if not raw:
        return False
    if b'\x00' in raw[:2048]:
        return True
    sample = raw[:2048]
    non_text = sum(1 for b in sample if b < 9 or (13 < b < 32))
    return (non_text / max(1, len(sample))) > 0.2


def choose_text_parser(extension: str, decoded: str, shebang: str | None) -> str:
    lowered = decoded.lower()
    if extension == '.py' or 'import ' in decoded or '@commands.' in decoded:
        return 'python_like'
    if extension in {'.yml', '.yaml'} or 'services:' in lowered:
        return 'yaml_like'
    if extension == '.json' or lowered.strip().startswith('{'):
        return 'json_like'
    if extension == '.html' or '<html' in lowered:
        return 'html_like'
    if extension == '.sh' or shebang:
        return 'shell_like'
    return 'text_decode'


def determine_modality(extension: str, parser_used: str, text_excerpt: str, strings_excerpt: list[str]) -> str:
    lowered = text_excerpt.lower()
    if parser_used == 'python_like':
        return 'code_python'
    if parser_used == 'yaml_like' and 'services:' in lowered:
        return 'config_compose'
    if parser_used == 'shell_like':
        return 'script_shell'
    if '#general' in lowered or 'role:' in lowered or 'guild' in lowered:
        return 'discord_note'
    if strings_excerpt:
        return 'binary_with_strings'
    if extension in TEXT_EXTENSIONS:
        return 'text_document'
    return 'unknown'


def extract_strings(raw: bytes) -> list[str]:
    decoded = raw.decode('utf-8', errors='ignore')
    return [part.strip() for part in re.split(r'[^A-Za-z0-9_#./:-]+', decoded) if len(part.strip()) >= 4][:120]


def path_hint_tokens(rel_path: str) -> list[str]:
    parts = re.split(r'[^A-Za-z0-9]+', rel_path.lower())
    return [part for part in parts if part]
