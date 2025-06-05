# 모든 pytest 파일은 test_ 로 시작해야 한다


# 함수를 선언할 때는 항상 pytest 표준에 따라 테스트 메서드 이름을 작성해야 한다.
# 즉, 메서드 이름은 항상 test 라는 키워드로 시작해야 한다.
def test_firstProgram():
    print('hello')

# 모든 코드는 메서드로 감싸야 한다.