#multiple inheritance


class classB:
    def printdata(self):
        print(20)
class classc:
    def printdata(self):
        print(3)
class ClassA(classB,classc):
    pass
a = ClassA()
a.printdata()
