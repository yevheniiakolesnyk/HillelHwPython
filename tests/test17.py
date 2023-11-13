from src import func17


def test_add():
    assert my_func17.add(2, 3)

def test_minus():
    assert my_func17.minus(4, 1)

def test_multiple():
    result = my_func17.multiplying(3, 12)
    assert isinstance(result, int), f"Expected an integer, but got {type(result)}"

def test_division():
    assert my_func17.division(6, 2)

def test_square():
    assert my_func17.square(4)
