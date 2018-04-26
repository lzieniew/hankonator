# coding=utf-8
from widgets import Stage4Window


def test_create_window():
    win = Stage4Window(None, None, None)
    assert win is not None
