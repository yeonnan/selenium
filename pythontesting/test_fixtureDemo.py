import pytest


@pytest.fixture()
def setup():
    print('첫번째~')
    yield
    print('나중에')


def test_fixtureDemo(setup):
    print('-----')