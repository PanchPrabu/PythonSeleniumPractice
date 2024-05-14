import pytest


@pytest.mark.smoke
@pytest.mark.skip

def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "This test case gets failed because condition not matches"


def test_secondcc2program():
    a=4
    b=2
    a+2 ==6 ,"Additon not matches"

