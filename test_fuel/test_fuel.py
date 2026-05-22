from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("5/dog")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("-1/2")


def test_guage():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
