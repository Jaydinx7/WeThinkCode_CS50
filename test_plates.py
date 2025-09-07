from plates import is_valid

def test_length():
    assert is_valid("AABBCC") == True
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AABBCCDD") == False

def test_first_letters_alpha():
    assert is_valid("AA1234") == True
    assert is_valid("AA") == True
    assert is_valid("12") == False
    assert is_valid("123456") == False

def test_alphanumeric():
    assert is_valid("AB?><:") == False
    assert is_valid("Hello!") == False

def test_end_numbers():
    assert is_valid("AA1234") == True
    assert is_valid("AA15BB") == False

def test_no_zero_start():
    assert is_valid("AA1230") == True
    assert is_valid("AA0123") == False
