#LearningConstrutors
class Calculator:
    num=100

    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b
        print("I will be called Automatically")
    def getData(self):
        print("PythonTesting")
    def summation(self):
        return self.firstnumber+self.secondnumber+Calculator.num

obj=Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.summation())

obj1=Calculator(10,26)
obj1.getData()
print(obj1.num)
print(obj1.summation())