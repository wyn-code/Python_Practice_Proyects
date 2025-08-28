my_set = set((1,2,3,4,5,6,(1,2,3)))
print(type(my_set))
print(len(my_set))
print(2 in my_set)

## Union de sets
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
s1.remove(2)
s1.discard(6)

sorteo = s1.pop()
print(sorteo)

s1.clear()
print(s1)

