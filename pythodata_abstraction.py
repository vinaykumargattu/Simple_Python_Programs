#Data abstraction in python - attribute will not be visible outside of the class through the object.

class School():

    __name ="vinay kumar gattu"
    def __init__(self):
        print("the class contains name ", self.name)
class Student(School):
    def studentinfor(self):
        print("the student informatino is ", self.name)

s=Student()
s.studentinfor()