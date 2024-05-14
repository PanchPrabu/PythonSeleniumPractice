import pytest

def test_firstprogram(setup):
    print("Hello, this is my first Pytest Program")

@pytest.mark.smoke
@pytest.mark.xfail
def test_secondcc1program():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])