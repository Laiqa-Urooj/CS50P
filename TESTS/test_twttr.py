import pytest
from twttr import shorten

#Test with vowels
def test_string() :
    assert shorten("Laiqa") == "Lq"
    
#Test with mixed string i.e. numbers and string
def test_mix() :
    assert shorten("Pizza123") == "Pzz123"

#Test with numbers
def test_numbers() :
    assert shorten("12345") == "12345"
   
#Test with uppercase vowels 
def test_uppercase():
    assert shorten("AEIOU") == ""
 
#Test ith lower_case vowels   
def test_lowercase():
    assert shorten("aeiou") == ""

#Test without vowels
def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

#Test with punctuation
def test_punctuation():
    assert shorten("Hi!") == "H!"
    assert shorten("What's up?") == "Wht's p?"


