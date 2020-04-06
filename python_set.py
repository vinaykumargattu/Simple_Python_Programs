#using curly braces

let={"a", "b", "c"}
print(let)
print(type(let))
for i in let:
    print(i)

#using set() method

days =set(["sunday", "monday", "wednesday"])
print("before add the data", days)
days.add("Friday")
print("After add the data", days)
print(type(days))

for i in days:
    print(i)

#To add more than one item in the set, Python provides the update() method.

see =set(["car", "geep", "van"])
print("Before update the set informatojn", see)
see.update(["lorry", "bus", "truck"])
see.discard("lorrysd");
see.remove("bus");
print("After update the set information", see)

#using union | operator

s1 = {"a", "b", "c"}
s2 = {"x", "b","z"}
s2.pop()
print(s1-s2)
print(s1.difference(s2))
print(s1|s2)
print(s1.union(s2))
print(s1&s2)
print(s1.intersection(s2))

fset = frozenset([1,2,3,4,5])
fset.pop()



