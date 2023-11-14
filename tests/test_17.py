import pytest
from src import func_17

def test_add():
    assert func_17.add(2, 3)

def test_minus():
    assert func_17.minus(4, 1)

def test_multiple():
    result = func_17.multiplying(3, 12)
    assert isinstance(result, int), f"Expected an integer, but got {type(result)}"

def test_division():
    assert func_17.division(6, 2)

def test_square():
    assert func_17.square(4)