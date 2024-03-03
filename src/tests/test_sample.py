import pytest
from helper.helper_test import *


def test_answer():
    assert sum(3, 1) == 4


def test_mytest():
    with pytest.raises(
        SystemExit
    ):  # This line is checked the context manager of the pytest it raised the SystemExit exception or not. If raise the SystemExit exception the it passed otherwise it's failed
        raise_system_exit_exception()
