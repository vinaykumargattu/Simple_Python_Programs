
#Python Data Types

#Type 1 Numbers

a=12
print(a, type(a))

b=12.5;
print(b, type(b))

c=12.5j

print(c, type(c))

#Type 2 Strings

name="vinaykumar"

print(name, type(name))
#Below line gives the first letter of the string
print(name[0])
#Below line print the string 2 times
print(name*2)

#if we want to print specific string information

print(name[5:10])

#Type 3 List

list_s=[10,"Vinay Kumar", 33]

list_s[1]="shivakumar"

print(list_s)
print(list_s[0])
print(list_s[1])
print(list_s[2])
print(list_s[0:3])

print(id(list_s[1]))

#Type 4 Tuple

t=(15,"Shiva Kumar", 33)

print(t)
print(t[0])

d={1:10, 2:"Shiva Kumar"}
print(d[2], type(d[2]))
print(d[1], type(d[1]))
print(d.keys())
print(d.values())


