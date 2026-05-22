import pytest

from working import convert

def test_first():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    with pytest.raises(ValueError):
        assert convert("10:30 PM 10 AM")
    with pytest.raises(ValueError):
        assert convert("12:60 AM to 10:00 PM")

