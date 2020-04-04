#Python If-else statements

x=int(input("Enter x value"))
y=int(input("Enter y value"))
z=int(input("Enter z value"))


if x>y:
    print("x is greter than y")

elif x>y and x>z:
    print("x is large number")
elif y>x and y>z:
    print("y is large number")
elif z>x and z>y:
    print("z is large number")
else:
    print("Non of the above")