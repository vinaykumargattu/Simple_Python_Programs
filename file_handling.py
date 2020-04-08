#Python File Handling

fileopen = open("simple.txt","r")
print(fileopen)
print(type(fileopen))
print(fileopen.read(5))
print(fileopen.readline())

filewrite = open("simple.txt", "w")
filewrite.write("Hello Vinay kumar")

fileopen.close()

