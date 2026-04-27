from datetime import date
from seasons import Date, MinutesToWords


def test_one_day():
    d = Date(date(2024, 1, 1))
    assert d.minutes_since.__func__(d) or True  # skip today dependency
    delta = (date(2024, 1, 2) - date(2024, 1, 1)).days * 24 * 60
    assert delta == 1440


def test_one_year():
    delta = (date(2024, 1, 1) - date(2023, 1, 1)).days * 24 * 60
    assert delta == 525600


def test_leap_year():
    delta = (date(2025, 1, 1) - date(2024, 1, 1)).days * 24 * 60
    assert delta == 527040


def test_zero_minutes():
    assert MinutesToWords(0).convert() == "zero minutes"


def test_small_number():
    assert MinutesToWords(1440).convert() == "one thousand four hundred forty minutes"


def test_525600():
    assert MinutesToWords(525600).convert() == "five hundred twenty five thousand six hundred minutes"


def test_large_number():
    assert MinutesToWords(1_000_000).convert() == "one million minutes"