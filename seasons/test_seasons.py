from seasons import edited

def test_date():
    assert edited("2026-05-08") == "One thousand, four hundred forty minutes"
    assert edited("2026-04-08") == "Forty-four thousand, six hundred forty minutes"


def test_validity():
    try:
        edited("january 1 2026")
    except SystemExit as e:
        assert str(e) == "Invalid date"





