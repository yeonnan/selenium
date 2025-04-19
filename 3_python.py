# if
greeting = 'good morning'
a = 4

# if greeting == 'good morning':
if a>2:
    print('ifififif')
    print('second linne')
else:
    print('else')
print('if else condition code is completed')


# for loop
# 반복문 : 리스트의 모든 요소를 반복하게 해줌
# for - 선언해야 하는 변수로 반복하게 됨 / in - 반복하는 대상
obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i*2)

# 자연수의 합계
sum = 0
for j in range(1, 6):       # range(i,j) -> 1 to j-1
    sum += j
print(f'sum : {sum}')


print('---------------------')
for k in range(1, 10, 5):
    print(k)

for m in range(10):
    print(f'm : {m}')