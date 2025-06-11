# 모든 pytest 파일은 test_ 로 시작해야 한다

# 함수를 선언할 때는 항상 pytest 표준에 따라 테스트 메서드 이름을 작성해야 한다.
# 즉, 메서드 이름은 항상 test 라는 키워드로 시작해야 한다.


import pytest

@pytest.mark.smoke   
def test_firstProgram(setup):
    print('hello')


# @pytest.mark.xfail : 아래의 메서드가 실행은 되지만 결과값에 포함되지 않음 -> 실행은 하지만 보고는 안함
@pytest.mark.xfail
def test_greet():
    print('good morning')


def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])