# pytest - Unit testing for functions.py

import functions
import pytest
import sys


# Skip a test based on python version
@pytest.mark.skipif (sys.version_info < (3,5), reason="Not currently needed")
def test_calc_total():
  total = functions.calc_total(4,5)
  assert total == 9


def test_calc_multiply():
  result = functions.calc_multiply(10,3)
  assert result == 30

def test_dummy():
  assert True



