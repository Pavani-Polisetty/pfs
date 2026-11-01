#anomymous function
'''
add=lambda x,y:x+y
print(add(10,20))

result=lambda x,y,z,n:[x,y,z,n]
print(result("python","cython","java","bava"))


print((lambda x,y:x+y)(10,20))

print((lambda x:"even" if x%2==0 else "odd")(10))


print((lambda n:"even" if n%2==0 and n>5 else "odd" if  n%2!=0 else "not")(15))

s = input()
print((lambda s:"valid" if len(s)>5 and len(s)<12 else "Invalid")(s))


print((lambda n:[i for i in range(n)])(5))


x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
    else:
        l.append("odd")
print(l)


#List comprehension
#when using onlyif 
print([i for i in x if i%2==0]) 

#when using both if and else
print([i if i%2==0 else "odd" for i in x])

#set comprehension
print({i if i%2==0 else "odd" for i in x})


#dict comprehension
x =[7,8,9,1,2,3,4]
print(i:"even" )


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [j for i in a for j in i]

print(res)


overs = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4]]

balls = [ball for over in overs for ball in over]

print(len(balls))




print(list(map(lambda x:"even" if x%2==0 else "odd",[1,2,3,4,5,6])))



print(list(map(lambda x:"even" if x%2==0 else x,[1,2,3,4,5,6])))


print(list(map(lambda x:"even" if x%2==0 else x,[1,2,3,4,5,6])))

#output - [1, 'even', 3, 'even', 5, 'even']

x = ["a","b","c","d","e"]
print(tuple(map(lambda x :x.upper(),x)))

#output ('A', 'B', 'C', 'D', 'E')

prices=[900,1000,800,700,600,200,1200]
result=map(lambda x:x if x>500 else "not",prices)
print(list(result))

#filter
prices=[900,1000,800,700,300,200,1200]
result=filter(lambda x:x<500,prices)
print(list(result))


names = ["Python","Cython","Pardhu","Paul","john"]
result = filter(lambda x:x.startswith("P"),names)
print(list(result))

import functools
prices = prices=[900,1000,800,700,300,200,1200]
result = functools.reduce(lambda x,y:x+y,prices)
print(result)


print(help(functools))



#all and any methods
x=["sirs","madam","sir","anthey"]
print(all(len(i)>3 for i in x ))

x=["sirs","madam","sir","anthey",1]
print(all(type(i)==str for i in x ))


x=["sirs","madam","sir","anthey",1]
print(any(type(i)==int for i in x ))


'''
def Generator(n):
    for i in n:
        yield i
    
    
n=["1file","7file","3file","4file","5file"]
result=Generator(n)
print(next(result))
print(next(result))
print(next(result))


for i in range(len(n)):
    print(result.__next__())


#print(list((i for i in range(4))))


result=(i for i in range(4))

print(list(result))


def Python():
    yield 10
    yield 20
    yield 200
#     return 1
#     return 2
    
result=Python()
# print(result)
# print(result)
#print(next(result))
print("1done")
for i in range(3):
    print(result.__next__())



d={}
def Register():
    username = input("Enter username: ")
    if len(username) >= 2 and len(username) <= 12:
        password = input("Enter password: ")


        if len(password) >= 6 and len(password) <= 10:
            print("Registration successful")
            return username, password
        else:
            print("Password must be 6-10 characters")
            return None, None
    else:
        print("Username must be 2-12 characters")
        return None, None




def Login(reg_username, reg_password):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == reg_username and password == reg_password:
        print("Login successful")
    else:
        print("Invalid username or password")



while True:
    print("1.Register\n2.Login")
    choose=int(input())
    if choose==1:
        Register()














































































