import pytest
from calculator import Calculator


def test_precise_addition(precise_calculator):
    assert precise_calculator.add(1.0 / 3, 1.0 / 3) == pytest.approx(0.67)

@pytest.mark.parametrize("precise_calculator_with_precision, expected", [
    (2, 0.67),
    (3, 0.667),
    (4, 0.6667),
], indirect=["precise_calculator_with_precision"])
def test_precise_addition_parameterized(precise_calculator_with_precision, expected):
    assert precise_calculator_with_precision.add(1.0 / 3, 1.0 / 3) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [(3, 5, 8), (1, 1, 2), (-1, -1, -2), (-1, 5, 4), (0, 0, 0)])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (1, 5, -4), (-5, -3, -2), (0, 0, 0), (10, 5, 5)])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(2, 5, 10), (-3, 4, -12), (1.5, 2, 3.0), (2.0, 2.5, 5.0), (0, 10, 0)])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("a, b, expected", [(10, 2, 5), (5, 2, 2.5), (6, 3, 2.0)])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == pytest.approx(expected)

def test_divide_by_zero_raises(calculator):
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),  # Should be 1/(2^2) = 0.25
    (10, -1, 0.1), # Should be 1/10 = 0.1
    (-2, 3, -8)   # Including a negative base
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (5, 120),
    (10, 3628800),
])
def test_factorial_parameterized(calculator, n, expected):
    assert calculator.factorial(n) == expected

@pytest.mark.parametrize("n", [-1, -5, -10, -2.5, "abc"])
def test_factorial_invalid_parameterized(calculator, n):
    with pytest.raises(ValueError):
        calculator.factorial(n)

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (7, 13),
    (10, 55),
])
def test_fibonacci_parameterized(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

@pytest.mark.parametrize("n", [-1, -3, -7, -1.5, "def"])
def test_fibonacci_invalid_parameterized(calculator, n):
    with pytest.raises(ValueError):
        calculator.fibonacci(n)