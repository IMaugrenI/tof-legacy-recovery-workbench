from tof_workbench.acceptance import TARGET_CLASSES


def test_target_class_set_is_stable() -> None:
    assert TARGET_CLASSES == {'discord', 'bot', 'repo', 'review_required'}
