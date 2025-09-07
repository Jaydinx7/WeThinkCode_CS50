from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("   Hello   ") == 0
    assert value("Hello there") == 0

def test_h():
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("   Hi   ") == 20
    assert value("Hi there") == 20

def test_no_h():
    assert value("Yo") == 100
    assert value("whats up") == 100
    assert value("   Sup   ") == 100
    assert value("123 Greetings 123") == 100
