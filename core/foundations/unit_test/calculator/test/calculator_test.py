import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import calculator

def test_addition():
    assert calculator.addition(2, 3) == 5

def test_subtraction():
    assert calculator.subtraction(5, 2) == 3

def test_multiplication():
    assert calculator.multiplication(3, 4) == 12

def test_division():
    assert calculator.division(10, 3) == 3

def test_modulus():
    assert calculator.modulus(10, 3) == 1
