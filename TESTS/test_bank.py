from bank import value
import pytest

#Test with hello
def test_hello() :
    assert value("hello") == 0
#Test with hi
def test_hi() :
    assert value("hi") == 20
#Test with fine
def test_other_word() :
    assert value("Fine") == 100
#Test with numbers
def test_numbers() :
    assert value("123") == 100