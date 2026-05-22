from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar()

    jar.deposit(3)

    assert str(jar) == "🍪🍪🍪"

def test_withdraw():
    jar = Jar(10)

    jar.deposit(7)
    jar.withdraw(3)

    assert jar.size == 4

def test_deposit():
    jar = Jar(10)

    jar.deposit(5)

    assert jar.size == 5
    with pytest.raises(ValueError):
        Jar(-1)
