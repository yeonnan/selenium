# 함수 : 특정 작업을 수행하는 연관된 문장의 그룹
# 함수를 호출하려면, 해당 함수의 이름을 호출하면 된다. 그럼 자동으로 함수에 속한 모든 문장이 실행

def hello(name):
    print('굿모닝'+name)

def addInteger(a,b):
    return a+b

hello('aa')
print(addInteger(5, 7))