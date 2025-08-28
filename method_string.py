text = "This is Bruno's text"
result = text.split("s")
print(result)

a = "Learning"
b = "Python"
c = "is"
d = "genial"
e= "-".join([a,b,c,d])
print(e)

f = text.find("is")
print(f)

r = text.replace("Bruno's", "my Love's")
g = text.replace("s", "z")
print(r)
print(g)