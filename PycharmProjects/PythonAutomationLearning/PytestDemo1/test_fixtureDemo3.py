import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will be executing the steps of fixture demo method")

    def test_fixtureDemo1(self):
        print("I will be executing the steps of fixture demo1 method")

    def test_fixtureDemo2(self):
        print("I will be executing the steps of fixture demo2 method")

    def test_fixtureDemo3(self):
        print("I will be executing the steps of fixture demo3 method")