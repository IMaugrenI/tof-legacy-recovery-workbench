from tof_workbench.cli import build_parser


def test_cli_has_core_commands() -> None:
    parser = build_parser()
    sub = next(action for action in parser._actions if getattr(action, 'choices', None))
    assert {'run', 'acceptance', 'clean'}.issubset(set(sub.choices))
