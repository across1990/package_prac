import pytest

def test_non_empty_string():
    assert is_palindrome("abc") is False
    assert is_palindrome("aba") is True
    
def test_empty_string():
    assert is_palindrome("") is True
    
def test_wrong_type():
    with pytest.raises(ValueError):
        assert is_palindrome(123)