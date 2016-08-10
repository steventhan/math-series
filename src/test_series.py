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


def test_sum_series_fibonacci():
    from series import sum_series
    assert sum_series(2) == 0
