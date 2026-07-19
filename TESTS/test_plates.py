from plates import is_valid
import pytest

#Test correct plate
def test_correct_plate():
    assert is_valid("CS50") == True
#Test plate starting with number
def test_starts_with_number():
    assert is_valid("50cd") == False
#Test plate with minimum characters
def test_minlength():
    assert is_valid("C") == False
#Test plate with number in middle
def test_number_in_middle():
    assert is_valid("CS50D") == False
#Test plate with 0 as first number
def test_0_as_first_number():
    assert is_valid("CS04") == False
#Test with max length
def test_maxlength():
    assert is_valid("CSDEFC50") == False
#Test with punctuation
def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS,50") == False
#Test with spaces
def test_spaces():
    assert is_valid("CS 50") == False
#Test with minimum valid length
def test_exact_minimum():
    assert is_valid("CS") == True
#Test with maximum valid length
def test_exact_maximum():
    assert is_valid("ABC123") == True
#Test with first number not 0
def test_valid_number():
    assert is_valid("CS50") == True
