from fuel import convert, gauge
from pytest import raises

def test_convert_fraction():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_gauge_percentage():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"

def test_convert_errors():
    with raises(ValueError):
        convert("12")
    with raises(ValueError):
        convert("2/1")
    with raises(ValueError):
        convert("-1/2")
    with raises(ZeroDivisionError):
        convert("0/0")

