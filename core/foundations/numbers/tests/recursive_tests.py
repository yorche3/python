from numbers import (
  sum_of_first_n_rec,
  factorial_rec,
  fibonacci_rec,
  greatest_common_divisor_rec,
  least_common_multiple_rec,
)

def test_sum_of_first_n_rec():
    assert sum_of_first_n_rec(0) == 0
    assert sum_of_first_n_rec(3) == 6

def test_factorial_rec():
    assert factorial_rec(0) == 1
    assert factorial_rec(4) == 24

def test_fibonacci_rec():
    assert fibonacci_rec(0) == 0
    assert fibonacci_rec(1) == 1
    assert fibonacci_rec(6) == 8

def test_greatest_common_divisor_rec():
    assert greatest_common_divisor_rec(12, 8) == 4
    assert greatest_common_divisor_rec(7, 5) == 1

def test_least_common_multiple_rec():
    assert least_common_multiple_rec(4, 6) == 12
    assert least_common_multiple_rec(6, 8) == 24
