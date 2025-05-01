'''
# 상속 : 부모 클래스의 프로퍼티를 얻는 것
# 부모 클래스에서 선언하고, 부모 클래스에서 자식 클래스로 상속한다.

from 6_python import Calculator -> 숫자로 시작하는 파일은 파이썬이 모듈로 인식하지 못함
영어로 변경하면 되지만 숫자로 하고 싶다면 importlib 사용
'''

import importlib

# '6_python'이라는 이름의 모듈을 동적으로 import
calculator_module = importlib.import_module("6_python")

# 그 안에 있는 Calculator 클래스 사용
Calculator = calculator_module.Calculator

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())