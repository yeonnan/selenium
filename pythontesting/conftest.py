'''
파일명은 반드시 conftest
이 파일에서 픽스쳐를 선언하면 이 폴더들 안에 있는 모든 테스트 파일에서 픽스쳐 사용 가능
(모든 테스트 파일 : 모든 pytest 테스트 파일)
'''

import pytest


@pytest.fixture(scope='class')
def setup():
    print('첫번째~')
    yield
    print('나중에')


@pytest.fixture()
def dataLoad():
    print('사용자 프로필 데이터 생성 중')
    return ['yeon', 'ahn', 'https://github.com/yeonnan']


@pytest.fixture(params=[('chrome', 'yeon'), 'Firefox', 'IE'])
def crossBrowser(request):
    return request.param