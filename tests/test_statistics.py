import sys
sys.path.append(".")

import pytest
from src.fyamaktestpypi import statistics

def test_mean():
    assert statistics.mean([1,2,3,4,5]) == 3
    