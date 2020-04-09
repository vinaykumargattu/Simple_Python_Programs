import json
from math import factorial

class Mymath():
    def __init__(self):
        a=5
        factval =factorial(a)
        print(type(factval))
        print(factval)
        print(factorial(a))


my = Mymath()

#The dir() function returns a sorted list of names defined in the passed module. 

list = dir(json)
print(list)