import pytest

from simple_py_project.app import load


def test_load_data():
    assert not load("")
    assert not load("asdf")