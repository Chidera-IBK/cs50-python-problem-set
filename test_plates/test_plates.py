from plates import is_valid

def test_valid():
    assert is_valid("AAA222") == True
def test_aphabetical():
    assert is_valid("12345") == False
def test_lenght():
    assert is_valid("ASKAJDHd") == False
def test_placement():
    assert is_valid("AA133A") == False
def test_zero_placement():
    assert is_valid("AAA032") == False
def test_alphanumeric():
    assert is_valid("AAAT.,") == False

