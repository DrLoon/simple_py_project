import pytest

from simple_py_project.app import load


def test_load_data():
    with pytest.raises(Exception):
        load("")
    with pytest.raises(Exception):
        load("asdf")