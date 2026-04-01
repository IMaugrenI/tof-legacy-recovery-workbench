from pathlib import Path

from tof_workbench.pathing import source_id_for_rel_path


def test_source_id_stable() -> None:
    assert source_id_for_rel_path('examples/bot_module.py') == source_id_for_rel_path('examples/bot_module.py')
