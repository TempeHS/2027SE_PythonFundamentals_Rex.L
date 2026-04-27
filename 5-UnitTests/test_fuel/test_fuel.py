from fuel import convert, gauge


def test_convert_normal():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_rounds():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_full():
    assert convert("4/4") == 100


def test_convert_empty():
    assert convert("0/4") == 0


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"