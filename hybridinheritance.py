# hydrid inheritances

class ClassA:
    def printdata(self):
        print("20")
class ClassB(ClassA):
     def printdata(self):
        print("30")
class ClassC(ClassA):
    def printdata(self):
        print("40")
class ClassD(ClassB,ClassC):
    pass
a = ClassD()
a.printdata()
