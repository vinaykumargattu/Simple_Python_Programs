import  re

string = "hello how are you, hello vinay kumar"
match = re.findall("hello", string)
match1 = re.search("hello", string)
print(match)
print(match1)
print(match1.span())
print(match1.group())
print(match1.string)
