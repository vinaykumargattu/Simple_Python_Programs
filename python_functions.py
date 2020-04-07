#Function calling

def simple_fuction():
    print("Hellow welcome to python functions")
simple_fuction()


#Parameters in function
def simple_namefunction(name):
    print("the name is come from outside of the functions", name)
simple_namefunction("vinay")

#Additions using Parameters in function

def simple_addition(a,b):
    print("Sum of a+b is ", a+b)
simple_addition(10,20)

#Passing Immutable Object (List)

def simple_list(list1):
    list1.append(40)
    list1.append(50)
    print("list inside the functions", list1)

list1 = [10,20,30]
simple_list(list1)
print("list outside the functions", list1)

#Passing Mutable Object (String)

def simple_string(str):
    str = str +"how are your"
    print("Print the string value inside the functions", str)
string1 = "Hello"
simple_string(string1)
print("Print the string value outside the functions", string1)

#Required arguments
def simple_requiredarguments(name):
    message = "hi" +name
    return message
name=input("Enter the name")
print(simple_requiredarguments(name))

#Keyword arguments will enable us to pass the arguments in the random order.

def simple_keywordargs(p,t,r):
    intrest =(p*t*r)/100
    return intrest
print("Intrest is ", simple_keywordargs(r=10,t=5,p=25,))

#Variable length Arguments

def simple_variablrargs(*names):
    print(type(names))
    print("printing the entered values")
    for name in names:
        print(name)
simple_variablrargs("shiva", "parvathi", "ganapathi", "ayyappa", "ganga")