from main import is_palindrome

def test_pytest():
    assert 2+2 == 4

def test_is_palindrome_happy():
    assert is_palindrome("radar") == True 
    assert is_palindrome("Radar") == True

def test_is_palindrome_unhappy():
    assert is_palindrome("radars") == False