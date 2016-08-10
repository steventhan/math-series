# TODO: add utf-8
import pytest

FIBONACCI_TABLE = [
    (-1, False),
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
]


@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_fibonacci(n, result):
    from series import fibonacci
    assert fibonacci(n) == result


LUCAS_TABLE = [
    (-1, False),
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29)
]


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    from series import lucas
    assert lucas(n) == result


# Using test sum_series func for fibonacci series
@pytest.mark.parametrize('n, result', FIBONACCI_TABLE)
def test_sum_series_fibonacci(n, result):
    from series import sum_series
    assert sum_series(n) == result

OTHER_SERIES_TABLE = [
    (-1, 5, 7, False),
    (0, 5, 7, 5),
    (1, 5, 7, 7),
    (2, 5, 7, 12),
    (3, 5, 7, 19),
    (4, 5, 7, 31),
    (5, 5, 7, 50),
    (6, 5, 7, 81),
    (7, 5, 7, 131)
]


# Using test sum_series func for a random series
@pytest.mark.parametrize('n, a, b, result', OTHER_SERIES_TABLE)
def test_sum_series_other(n, a, b, result):
    from series import sum_series
    assert sum_series(n, a, b) == result
