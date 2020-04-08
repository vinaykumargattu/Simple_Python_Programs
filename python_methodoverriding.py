#Real Life Example of method overriding

class School():
    def __init__(self):
        print("this is the init method")
class Student1(School):
    def name(self):
        return "shiva"

class Student2(School):
    def name(self):
        return "parvathi"
class Student3(School):
    def name(self):
        return "ganapathi,kumarswamy, ganga, nagaraju, nandi"
s = School()
s1 = Student1()
s2 = Student2()
s3 = Student3()
print(s)
print(s1.name())
print(s2.name())
print(s3.name())

