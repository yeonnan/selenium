# test.txt

file = open('test.txt')


# read 메서드 : 파일의 모든 콘텐츠를 읽을 수 있음
# 매개변수를 입력하여 특정 개수의 글자 읽기 -> file.read(5)
# print(file.read())

# readline : 한번에 한줄씩 파일 읽기
print(file.readline())
print(file.readline())


# 파일을 열때마다 마지막에는 파일을 꼭 닫아야 한다.
# 파일을 닫지 않으면 메모리가 새거나, 여러 파일을 연 경우 파일 손상
file.close()


# 줄별로 출력
