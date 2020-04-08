#Python Inheritance - ma derived class can inherit base class by just mentioning the base in the bracket after the derived class name.

class Mymath():
    #v1=''
   # v2=''
    def __init__(self,a,b):
        self.v1=a
        self.v2=b
        print("a value is %d"%a)
        print("b value is %d"%b)
    def add(self,v1, v2):
        print("a value is %d" % v1)
        print("b value is %d" % v2)
        print("a+b=", v1+v2)

class Cals(Mymath):
    print("This is inherited class")

print(issubclass(Mymath,Cals))
print(issubclass(Cals, Mymath))
my = Cals(10,20)
my.add(1,2);