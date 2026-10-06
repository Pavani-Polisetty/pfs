l=[1,"pavani"]
l.append("python")
print(l)

#append
l.append(["bsc",2])
print(l)


#extend
l.extend([5000,"python developer"])
print(l)


#insert
l.insert(1,["cse","institute"])
print(l)


#pop

print(l.pop())
print(l.pop(0))

#remove

l.remove("python")
print(l)

l.reverse()
print(l)


#sort
x=[2,1,5,0,-1]
##print(x)
##x.sort(reverse=True) #for homogeneous data
##print(x)

print (sorted(x))
print(x)

#copy
y=x.copy()
print(y)
y.append(20)
print(x,y)
x.append(30)
print(x,y)

x.clear()
print(x)

del x

 
