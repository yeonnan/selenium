str1 = "https://github.com/yeonnan.com"
str2 = 'hello world'
str3 = 'github'

print(str1[1])       # t


# 전체 문자열에서 하위 문자열 추출
print(str1[:5])      # https


# 두개의 문자열 연결
print(str1 + str2)


# 문자열에 특정 문자가 존재하는지 여부 확인
print(str3 in str1)     # True


# 문자열 분리
var = str1.split('.')     
print(var)      # ['https://github', 'com/yeonnan', 'com']
print(var[0])       # https://github


# trim 이란? 테스트의 시작이나 마지막 부분의 공백 제거
# strip : 시작과 마지막의 공백을 잘라내는데 사용
str4 = ' great '
print(str4.strip())

# 시작부분의 공백은 제거하되, 마지막 부분 공백 남겨두기
print(str4.lstrip())        # 왼쪽공백 제거
print(str4.rstrip())        # 오른쪽공백 제거   ->  great