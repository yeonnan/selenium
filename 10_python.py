# file = open('test.txt')

# file.close()


'''
아래의 방법으로 사용하면 file.close()를 추가하지 않아도 된다.
자동으로 아래의 줄이 파일을 열고, 전체 실행이 완료된 후 열었던 파일을 닫음
-> 수동으로 파일을 닫는 단계(file.close)를 작성할 필요가 없음
'''
# 읽기 모드로 파일을 열고자 할 경우 -> r 입력
# 쓰기 모드로 파일을 열고자 할 경우 -> w 입력
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)