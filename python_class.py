#Creating simple classes in python

class Mymath():
    #value1=''
    #value2=''

    def __init__(self, a, b):
        self.value1=a
        self.value2=b
        print("a value is %d"%a)
        print("b value is %d"%b)

    def myaddition(self):
        addition = self.value1+self.value2
        print("a value in my addition method is %d", self.value1)
        print("b value in my addition method is %d", self.value2)
        print(addition)
    def mysub(self):
        sub=self.value1-self.value2
        print(sub)

my = Mymath(20,25)
setattr(my,'value1', 55)
print(hasattr(my,'volue1'))
my.myaddition()
my.mysub()

print(getattr(my,'value1'))
print(getattr(my,'value2'))

print(my.__doc__)
print(my.__dict__)
#print(my.__name__)
print(my.__module__)

