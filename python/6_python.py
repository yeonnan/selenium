# class : 사용자가 정의한 청사진 또는 프로토타입

class Calculator:
    # 클래스 변수 : 클래스 내부에 즉시 정의하는 변수
    num = 100

    def __init__(self, a, b):
        self.firstnumber = a        # firstnumber : 인스턴스 변수 (생성자 안에서 정의하는 변수)
        self.secondnumber = b
        print('생성자~')

    def getData(self):
        print('메서드입니다')

    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num

obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())


# self 키워드 : 변수 이름을 메서드로 호출하는 데 필수
# 인스턴스 및 클래스 변수는 완전히 다른 목적을 가지고 있다. 하나는 객체에 첨부, 다른 하나는 객체에 첨부되지 않는다.
# 생성자 이름은 반드시 __init__
# 객체를 생성할 때 새로운 키워드는 필요하지 않다.