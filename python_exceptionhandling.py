#Exception handling in python try except elase
try:
    a = int(input("Enter a value"))
    b = int(input("Enter va value"))
    c=a/b
    print(c)
except Exception:
    print("0 Divide not possible")

else:
    print("good")

finally:
    print("this block will execute every time")
