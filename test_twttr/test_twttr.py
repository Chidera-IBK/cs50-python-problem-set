from twttr import shorten
import pytest



def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("rice") == "rc"
    assert shorten("chidera") == "chdr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("good-luck.") == "gd-lck."
    assert shorten("Davido001") == "Dvd001"


