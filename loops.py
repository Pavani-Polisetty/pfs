#loops
'''
for i in range(-10,-20,1):
    print(i)



d = {"name":"Pavani","age":60,"salary":56789}
for i in d:
    print(i)


x = {1,2,3,5,6,7}
for i in x:
    print(i)


for i in range(-20,0,1):
    print(i)



n=int(input()) #2
for i in range(1,11):
    print(f"{n}*{i}={n*i}")


n= int(input())
for i in range(1,11):
    if i%2==0:
        print(f"{n}*{i}={n*i}")

       #or
        
n = int(input())
for i in range(2,11,2):
    print(f"{n}*{i}={n*i}")



n = int(input())
for i  in range(1,11):
    if i==5:
        break
    else:
        print(f"{n}*{i}={n*i}")


n=int(input())
for i in range(1,11):
     if i%2==0:
        continue
    elif i>=6:
        break
    else:
        print(f"{n}*{i}={n*i}")



i=
while i>=0:
    print(i)
    i-=1

else:
    print("completed")




n= int(input())
i=5
while(i>=5):
    print(f"{n}*{i}={n*i}")
    i+=1




names = ["pushpa", "sravya", "venkannababu", "prabu", "pal", "lasya"]

for name in names:
    if not name.startswith('p'):
        print(name)

'''
n=int(input())
for number in range(1,n):
    for i in range(2,number):
        if number%i==0:
            break
    else:
        print(number)



















