from src.calculator import Calculator
import pytest

def test_add():
    cal = Calculator()
    assert cal.add(6) == 6

def test_subtract():
    cal = Calculator()
    cal.add(6)    
    assert cal.subtract(4) == 2

def test_divide():
    cal = Calculator() 
    cal.add(4)
    assert cal.divide(2) == 2

def test_zero_division():    
    with pytest.raises(ZeroDivisionError):
        cal = Calculator()
        cal.add(9)
        cal.divide(0)    

def test_multiply():
    cal = Calculator() 
    cal.add(2)
    assert cal.multiply(6) == 12

def test_nth_root():
    cal = Calculator()
    cal.add(9)
    assert cal.nth_root(2) == 3  

def test_reset():
    cal = Calculator() 
    cal.add(5)
    assert cal.reset() == 0  
