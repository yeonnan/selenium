import pytest


@pytest.mark.usefixtures('setup')
class TestExample:
    def test_fixtureDemo(self):
        print('real demo')

    def test_fixtureDemo1(self):
        print('demo1')

    def test_fixtureDemo2(self):
        print('demo2')

    def test_fixtureDemo3(self):
        print('demo3')