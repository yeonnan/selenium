'''
while
조건을 점검하기 위해 사용
조건이 True일 경우 무엇을 선언하든 계속해서 반복문 실행
조건이 False가 되기 전까지는 중지되지 않음
'''

it = 4

while it>1:
    if it!=3:
        print(it)
    it -= 1
print('while 종료')

print('--------------------')


# i가 5와 일치할 경우 break 적용
# 5가 존재할 경우 아래의 반복문에서 빠져나와 어떤 것도 실행되어서는 안되고 반복문을 완료해야 함
i = 10

while i>1:
    if i==5:
        break
    print(i)
    i -= 1
print('i / while 종료')

print('--------------------')


# continue : 특정 반복 건너뜀
j = 20

while j>1:
    if j==19:       # 20과 19가 동일하지 않기 때문에 실행되지 않고 아래 조건으로 이동
        j -= 1
        continue
    if j==5:        # 20과 5가 동일하지 않기 때문에 실행되지 않고 아래 조건으로 이동
        break
    print(j)
    j -= 1
print('j / while 종료')