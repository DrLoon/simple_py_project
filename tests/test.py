import pytest


def setup_module(module):
    # init_something()
    pass

from simple_py_project.app import load
def test_load_data():
    assert not load("")