from __future__ import annotations

import argparse
import asyncio
import shutil
from pathlib import Path

from .acceptance import run_acceptance
from .models import find_repo_root
from .pipeline import run_default_pipeline

GENERATED_DIRS = ['01_intake', '02_evidence', '03_hypotheses', '04_extracts', '05_mapping', '06_review', '07_reports']


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog='tof-workbench')
    sub = parser.add_subparsers(dest='command', required=True)

    run = sub.add_parser('run', help='Run the default workbench pipeline')
    run.add_argument('--repo-root', default='.')

    acc = sub.add_parser('acceptance', help='Run acceptance checks only')
    acc.add_argument('--repo-root', default='.')

    clean = sub.add_parser('clean', help='Remove generated stage directories')
    clean.add_argument('--repo-root', default='.')
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = find_repo_root(Path(args.repo_root))

    if args.command == 'run':
        summary = asyncio.run(run_default_pipeline(repo_root))
        print('Workbench run complete')
        print(summary)
    elif args.command == 'acceptance':
        payload = run_acceptance(repo_root)
        print('Acceptance complete')
        print(payload)
    elif args.command == 'clean':
        for name in GENERATED_DIRS:
            path = repo_root / name
            if path.exists():
                shutil.rmtree(path)
        print('Generated stage directories removed')


if __name__ == '__main__':
    main()
