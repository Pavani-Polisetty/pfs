s=set((1,2,3,4,5,6,7))
print(type(s))
s.add(20)
print(s)
s.update((9,6))
print(s)


x={1,2,3,4,5,6}
y={1,2,3,4,5,6,4,7,5,9}
print(x.union(y))
print(x | y)

print(x.intersection(y))
print(x & y)

print(x.difference(y))
print(x - y)

##print(x.symmetric_difference(y))
##print(x ^ y)
##print(x.issubset(y))


