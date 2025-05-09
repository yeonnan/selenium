print('hello')

# 주석주석


# 변수
a = 3
print(a)

str = ('hello world')
print(str)


b, c, d = 5, 6.4, 'aaa'

# 문자열과 정수 함께 출력하기
# 같은 문자열 끼리는 +로 연결 가능, 다른 자료형은 +로 연결 불가능
# print('b는 ' + b)       # TypeError: can only concatenate str (not "int") to str
print(f'b는 {b}')
print('{} {}'.format('b는', b))
print('d는 '+d)      # d는 aaa


# 자료형 종류 파악
print(type(b))      # <class 'int'>
print(type(c))      # <class 'float'>
print(type(d))      # <class 'str'>