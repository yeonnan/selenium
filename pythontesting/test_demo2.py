# 모든 pytest 파일은 test_ 로 시작해야 한다
# 함수를 선언할 때는 항상 pytest 표준에 따라 테스트 메서드 이름을 작성해야 한다.
# 즉, 메서드 이름은 항상 test 라는 키워드로 시작해야 한다.

# py.test -k 메서드명 -v -s : 특정 정규 표현식만 실행하도록 하는 명령어
# -k : 메서드 이름 실행을 의미 / -s : 결과에 로그 출력 / -v : 추가 정보
# 특정 파일만 실행하려면 py.test 파일명

# 마킹한 TC만 실행 : py.test -m 명칭 -v -s


import pytest

# 테스트를 마크하여 옵션 -m으로 실행할 수 있다
# @pytest.mark.명칭 : 하고 싶은 명칭으로 하면 해당 TC가 명칭으로 마킹됨
@pytest.mark.smoke
# @pytest.mark.skip : 전체 케이스가 실행될 떄 해당 마크만 skip
@pytest.mark.skip
def test_firstProgram():
    msg = 'hello'
    assert msg == 'hi', '문자열 달라서 실패'


def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == 6, 'XXXXX'
