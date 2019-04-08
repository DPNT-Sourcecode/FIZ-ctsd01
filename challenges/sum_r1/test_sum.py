import pytest
from sum import *

def test_one():
    assert(sum(1,1) == 2)

def test_two():
    assert(sum(2,2) == 4)

def test_three():
    assert(sum(0,1) == 1)
