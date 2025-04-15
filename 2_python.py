# 리스트에서는 모든 자료형 입력 가능
value = [1, 2, 'sam', 4, 5]

print(value[0])     # 첫번째 인덱스에 있는 값 출력 -> 1
print(value[2])     # 세번째 인덱스에 있는 값 출력 -> sam
print(value[-1])    # 마지막 인덱스 -> 5
print(value[1:3])   # 인덱스 1부터 시작하여 3전까지 출력 -> [2, 'sam']

# 리스트 사이에 값 삽입 - 'sam' 다음에 단어 추가하기
value.insert(3, 'aaaa')
print(value)        # [1, 2, 'sam', 'aaaa', 4, 5]

# 마지막에 값을 추가하려면 인덱스 수에 상관없이 append 사용
value.append('end')
print(value)        # [1, 2, 'sam', 'aaaa', 4, 5, 'end']

# 인덱스 값 업데이트 - 'sam' 자리에 다른 값 넣기
value[2] = 'newww'
print(value)        # [1, 2, 'newww', 'aaaa', 4, 5, 'end']

# 인덱스 값 삭제
del value[0]
print(value)        # [2, 'newww', 'aaaa', 4, 5, 'end']



# 튜플 - 리스트와 동일하지만, 변경 불가능한 불변형
val = (1, 2, 'sssam', 4.5)
print(val[1])       # 2

# val[2] = 'sa'
print(val)      # TypeError: 'tuple' object does not support item assignment



# 딕셔너리 - 키-값
dic = {'a':2, 4:'sa', 'c':'hello world'}
print(dic[4])       # 키가 4인 값의 sa
print(dic['c'])     # 키가 'c'인 값의 hello world


dict = {}
dict['firstname'] = 'ddddd'
dict['lastname'] = 'vvvvv'
print(dict)     # {'firstname': 'ddddd', 'lastname': 'vvvvv'}
print(dict['lastname'])     # vvvvv