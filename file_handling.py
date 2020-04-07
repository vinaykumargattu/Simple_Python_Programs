fileopne = open("simple.txt","r")
if fileopne:
    print("file opend sucessfully ")

content = fileopne.read(5)
compline = fileopne.readline()

print(type(content))
print(type(compline))
print(content)
print(compline)


fileopne.close();