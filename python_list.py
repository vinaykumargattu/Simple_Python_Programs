#Python List

"""list = ["a", "b", "c", "d", "e"]
list1 = ["f", "g", "h"]
list2=list+list1;
for i in list2:
    print(i)
   """
"""list = ["shiva", "ram", "krishna"]
list1 = [101, "shiva", 12]

list1.clear()
print("id is %d, Name is %s, Complex Number is %d "%(list1[0], list1[1], list1[2] ))
list1.append("kumar")
list1[0]
list1[1]
list1[2]
list1[3]
print(list1[3])
print(list1)
print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))
print(type(list[0]))

"""

# List copy using list.copy() function

list = ["vinay", "pavan"]
list2 =["kumar", "krishna"]

list3=list+list2

print(max(list3))
print(min(list3))

print(list3)
list1= list*2
print(list1)
print(len(list))

list.insert(3, "ram")
list.reverse()
#list.remove("vinay")


print(list)
print(list.count(list))
list1=list.copy();
print(list1)