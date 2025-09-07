from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_lower():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_mixed():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLlO") == "HLl"

def test_numbers():
    assert shorten("twitter 123") == "twttr 123"
    assert shorten("he3ll0") == "h3ll0"

def test_punctuation():
    assert shorten("Twitter?!.") == "Twttr?!."
    assert shorten("HELLO!!") == "HLL!!"
