from pathlib import Path

from tof_workbench.intake import is_input_metadata_file


def test_root_readme_is_input_metadata() -> None:
    root = Path('/tmp/00_input_alt')
    assert is_input_metadata_file(root / 'README.md', root) is True
    assert is_input_metadata_file(root / 'README_DE.md', root) is True
    assert is_input_metadata_file(root / 'examples' / 'discord_channels.txt', root) is False
