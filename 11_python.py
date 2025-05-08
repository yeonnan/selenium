ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception('실패실패')       # Exception: 실패실패
    pass


# 조건이 충족하지 않을 경우 실패하게 되는 방법
'''
assert 
조건을 예상하는 곳에서 사용할 수 있는 파이썬 메서드
조건은 항상 True에 해당해야 하며, 조건이 True가 아니라면 테스트 실패
'''
# assert(ItemsInCart==2)          # AssertionError


################


try:
    with open('aa.txt', 'r') as reader:
        reader.read()
except Exception as e:      
    # try 블록에 오류가 있을 때 except의 e 변수로 보내짐
    # 사용자 정의된 메시지를 제공하는 대신 e 변수 출력 가능 
    print(e)


#################


# try-except와 함께 사용. try-except의 실패나 성공 여부에 상관 없이 키워드 실행
finally:
    print('finally')