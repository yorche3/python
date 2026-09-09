from numbers import (
  sum_of_first_n_ite,
  factorial_ite,
  fibonacci_ite,
  greatest_common_divisor_ite,
  least_common_multiple_ite,
)

def test_sum_of_first_n_ite():
    assert sum_of_first_n_ite(0) == 0
    assert sum_of_first_n_ite(3) == 6

def test_factorial_ite():
    assert factorial_ite(0) == 1
    assert factorial_ite(4) == 24

def test_fibonacci_ite():
    assert fibonacci_ite(0) == 0
    assert fibonacci_ite(1) == 1
    assert fibonacci_ite(6) == 8

def test_greatest_common_divisor_ite():
    assert greatest_common_divisor_ite(12, 8) == 4
    assert greatest_common_divisor_ite(7, 5) == 1

def test_least_common_multiple_ite():
    assert least_common_multiple_ite(4, 6) == 12
    assert least_common_multiple_ite(6, 8) == 24
