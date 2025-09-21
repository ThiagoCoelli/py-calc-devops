from calculator.core import add, sub, mul, div
import pytest

def test_add_simple():
    assert add(2, 3) == 5.0
    assert add(-1, 1) == 0.0

def test_sub_simple():
    assert sub(10, 3) == 7.0
    assert sub(0, 5) == -5.0

def test_mul_simple():
    assert mul(4, 5) == 20.0
    assert mul(-2, 3) == -6.0

def test_div_simple_and_zero():
    assert div(10, 2) == 5.0
    assert div(3, 2) == 1.5
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
