# tests.py

import unittest
from get_files_info import get_files_info

def test_current_directory_get_files_info():
    result = get_files_info("calculator", ".")
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], str)
    assert result[0] == "main.py"

def test_pkg_directory_get_files_info():
    result = get_files_info("calculator", "pkg")
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], str)
    assert result[0] == "calculator.py"


def test_.._directory_get_files_info():
    result = get_files_info("calculator", "..")
    assert result is not None
    assert isinstance(result, list)
    assert len(result) > 0
    assert isinstance(result[0], str)
    assert result[0] == "main.py"





