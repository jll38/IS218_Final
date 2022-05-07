import os.path

import pytest

"""Tests if there is a log file"""
def test_logfile():
    assert os.path.exists("./app/logs/info.log")