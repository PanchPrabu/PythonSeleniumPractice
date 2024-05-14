#InheritanceConcepts
from constructors import Calculator


class childImpl(Calculator):
    num2=200

    def __init__(self):
        Calculator.__init__(self,2,10)
    def getCompleteDat(self):
        return self.num2+ self.num+self.summation()

obj=childImpl()
print(obj.getCompleteDat())