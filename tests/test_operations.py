from calculator.operations import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_add():
    assert add(3, 3) == 7

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 6) == 24