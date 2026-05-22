import pytest
from numb3rs import validate

def test_ipnum():
    assert validate("127.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_error():
    assert validate("192.168.001.1") == False
    assert validate("cat") == False
