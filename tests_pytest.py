from functions import (
    add, divide, multiply, subtract
)

import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (100, 200, 300),
    (-2, -5, -7),
    (2, 0, 2),
    (0, 0, 0),
    (1000000, 2000000, 3000000),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2.5, 3.6, 6.1),
    (-5.5, 2.5, -3.0),
])
def test_add_float(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    ("2", 3),
    (2, "3"),
    ("2", "3"),
    (None, 3),
    ([1, 2], 3),
    (2, True),
    (True, 3),
])
def test_add_type_error(a, b):
    with pytest.raises(TypeError):
        add(a, b)


@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (5, 8, -3),
    (6, 0, 6),
    (-3, -3, 0),
    (0, 10, -10),
    (-5, 3, -8),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (4.6, 1.4, 3.2),
    (3.14, 1.14, 2.0),
])
def test_subtract_float(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    ("5", 2),
    (5, "2"),
    (5, None),
    (5, [1, 2]),
])
def test_subtract_type_error(a, b):
    with pytest.raises(TypeError):
        subtract(a, b)


@pytest.mark.parametrize("a, b, expected", [
    (3, 0, 0),
    (3, 5, 15),
    (-3, -1, 3),
    (-14, 2, -28),
    (2, -3, -6),
    (3, 1, 3),
    (1, 0, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (-10, -2.5, 25.0),
    (5.2, 2, 10.4),
    (0.5, 0.5, 0.25),
    (-2, 0.5, -1.0),
])
def test_multiply_float(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    ("3", 2),
    (4, "5"),
    (3, None),
    (None, 5),
])
def test_multiply_type_error(a, b):
    with pytest.raises(TypeError):
        multiply(a, b)


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (-10, 2, -5.0),
    (10, -2, -5.0),
    (0, 5, 0.0),
    (-15, -3, 5.0),
    (7, 2, 3.5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (4.5, 3, 1.5),
    (4.5, 2.5, 1.8),
    (1, 3, 0.3333333333333333),
])
def test_divide_float(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [
    (10, 0),
])
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)


@pytest.mark.parametrize("a, b", [
    ("1", 3),
    (10, "1000"),
    (10, None),
    (None, 2),
])
def test_divide_type_error(a, b):
    with pytest.raises(TypeError):
        divide(a, b)