'''
l = [1,3,2,5,7,9,8]
empty = []
for i in range(len(l)):
    if i%2==0:
        empty.append(l[i])
        print(empty)

        

l = [1,2,4,6,7,8]
empty = []
for i in range(len(l)):
    if i%2==0:
        empty.append(l[i+1])
        print(empty)


#even index odd value  
l=[1,3,2,5,7,9,8]
empty = []
for i in range(len(l)):
  if(i%2==0):
    if(l[i]%2!=0):
        empty.append(l[i])
print(empty)


l=[1,3,2,5,7,9,8]
empty = []
for i in range(len(l)):
  n=l[i]**2
  empty.append(n)
print(empty)



#odd value add 10 even value add as it is 
l = [1,2,4,6,7,8]
empty = []
for i in l:
    if i%2!=0:
        empty.append(i+10)
    else:
        empty.append(i)
print(empty)        



l= [1,3,2,5,7,9,8]
l.reverse()
print(l)


l= [1,3,2,5,7,9,8]
empty = []
for i in range(len(l)-1,-1,-1):
    empty.insert(0,l[i])
    print(empty)


l= [1,3,2,5,7,9,8]
empty = []
for i in l:
    empty.insert(0,i)
    print(empty)




names = ['mohan','sravya','pavani','babu','lasya']
search = 'babu'
for i in names:
    if i == search:
        print("available")
        break
else:
    print("Not available")


#using for condition

names = ['mohan','sravya','pavani','babu','lasya']
empty = []
for i in range(len(names)):
    empty.append(len(names [i]))
print(empty)


#using while condition
names = ['mohan','sravya','pavani','babu','lasya']
empty = []
i= 0
while i<len(names):
    empty.append(len(names[i]))
    i+=1
print(empty)    
    


names = ['mohan','sravya','pavani','babu','lasya']
i= 0
d ={}
while i<len(names):
    d[names[i]]=len(names[i])
    i+=1
print(d)    


'''





















