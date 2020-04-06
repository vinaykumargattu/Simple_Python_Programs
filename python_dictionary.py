#Creating the dictionary and finding keys and values

emp={"name":"vinay", "age":22}

print(type(emp))
print(emp.keys())
print(emp.values())

print("Before modificatoin")
for a in emp:
    print(emp[a])

emp["name"]="kumar"
emp["age"] =25

print("after modificatoin")
for a in emp:
    print(emp[a])
#Accessing the dictionary values using normal way and for loop

print("Name is %s" %emp["name"])
print("Age is %d"%emp["age"])

for k in emp:
    
    print(k)
for i in emp:
    print(emp[i])