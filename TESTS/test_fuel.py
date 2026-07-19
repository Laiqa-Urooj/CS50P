from fuel import convert,gauge
import pytest

#Test convert
#Test to see happy flow
def test_normal() :
    assert convert("3/4") == 75
#Test to see zero division
def test_zero() :
    with pytest.raises(ZeroDivisionError) :
        4/0
#Test with wrong format
def test_format() :
    with pytest.raises(ValueError) :
        convert("3//4")
#Test with x > y
def test_greater() :
    with pytest.raises(ValueError) :
        convert("4/1")

#Test gauge
#Test to see F
def test_F() :
    assert gauge(99) == "F"
#Test to see E
def test_E() :
    assert gauge(1) == "E"
#Test happy flow
def test_correct() :
    assert gauge(75) == "75%"
