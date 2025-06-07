def test_firstProgram():
    msg = 'hello'
    assert msg == 'hi', '문자열 달라서 실패'


def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == 6, 'XXXXX'


# py.test -k 메서드명 -v -s : 특정 정규 표현식만 실행하도록 하는 명령어
# -k : 메서드 이름 실행을 의미 / -s : 결과에 로그 출력 / -v : 추가 정보
# 특정 파일만 실행하려면 py.test 파일명