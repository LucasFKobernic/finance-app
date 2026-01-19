import pytest

import sys
sys.path.append("../src")

from moduleA import add

def test_add_positive_numbers():
    a = 1
    b = 1

    result = add (1,1)
    assert result == 2