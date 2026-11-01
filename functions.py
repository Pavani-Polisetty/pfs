#funcions
'''
def wish(name):
    print(f"{name}good morning.you are the only one who completed the given task")


wish("Pavani")
print(type(wish))


def addition(a,b,c):
    print(a+b+c)

x,y,z = map(int,input().spli())
addition(x,y,z)


def Addition(a,b,c):
    return a+b+c
    
x,y,z=map(int,input().split())
print(Addition(x,y,z))

#positional arguments
#positional arguments follows keyword argument
def Stduents(name,marks):
    print(f"name:{name},marks:{marks}")
    
    
Stduents("john",322)
Stduents(678,"sai")


#keyword arguements
def Stduents(name,marks,place="vijawada"):
    print(f"name:{name},marks:{marks},place:{place}")
    
    
Stduents("john",322) #positional

Stduents(place="hyderbad",marks=678,name="sai")


#default arguments
def Stduents(name,marks,place="vijawada"): #defualt
    print(f"name:{name},marks:{marks},place:{place}")
    
    
Stduents("john",322) #positional

Stduents("sai",place="hyderbad",marks=678)  #keyword arguments


#variable length arguments
def Cal(*Values):#*will seperate the values from tuple
    print(*Values)#it will unpack
    print(sum(Values))
    
    
Cal(1,2,3)
Cal(1,2,3,4,5,7,8,8,7,77)



def Paradise(*items):
    print(*items)
    
Paradise("Biryani", "Pizza", "Burger", "Dosa")



def Order(**items):
    print(items)

Order(chicken = 1,biryani = 2)#when we pass "" it will give error   



def armstrong(n):
    temp = n
    total = 0
    power = len(str(n))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10

    if total == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


n = int(input())
armstrong(n)

def Order(**items):
    print(items)

if __name__=="__main__":
    Order(chicken=1,biryani=2)

  
def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end = " ")
        print()

pattern(5)


def StudentInfo(id,name, **subMarks):
    print(f"Average marks of {name} ({id}) is {sum(subMarks.values())/len(subMarks.values())}")
StudentInfo(1, "John", python=90, sql=70)


#local variable
def Local():
    x = 10
    print(x)
    
Local()

#global variable
name = "codegnan"
def Local():
    x = 10
    print(x)
    print(f"{name} local")
Local()
print(f"{name} global")

#changing local to global
name="codegnan"     #global
def Local():
    global name
    name="techgnan"
    print(f"{name} local ")
    
Local()

print(f"{name} global")


#nested function

def Main():
    print("this is a main function")
    
    def Inside():
        print("this is inner function")
        
    
    Inside()
    
Main()


#nesetd functions
def Netflix(ruser,pin):
    username=input()
    password=int(input())
    if username==ruser and pin==password:
        def Inside(sub):
            if sub=="yes":
                print("this is inner function")
            else:
                print("no subscription")
            
        sub=input()
        Inside(sub)

    else:
        print("not found")
Netflix("john",12345)

#nested functions
def Purchase(amount,offer="no"):
    if offer=="yes":
        def Offer(discount):
            return amount-discount
        
        print(Offer(200))
    else:
        print(f"you have to pay {amount}")
        
    
amount=int(input())
offer=input()
Purchase(amount,offer)



#pass by value and pass by reference

def Fun(x):
    x=20
    print(x)
    
    
x=int(input())
Fun(x)
print(x)


def Fun(x):
    print(x)
    
    x.append(99)
    print(x)
    
    
y=[1,2,3,4]
Fun(y)

print(y)


#pass by reference
def Fun(x):
    x.append(99)
    print(x)
    
y=[1,2,3,4]
Fun(y)

print(y)


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input())
fibonacci(n)

#anagram
def Anagram(s1,s2):
    d1={};d2={}
    if len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
                
            #word2
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1
                
        if d1==d2:
            print("anagram")
        else:
            print("not")
                
            
    else:
        print("not a anagram")
                 
    
s1="Heart"
s2="Earth"
Anagram(s1.lower(),s2.lower())


def Number(n):
    if n == 10:
        return
    else:
        print(n)
        Number(n+1)

Number(1)       



def Number():
    if n == 0:
        return
    else:
        print(n)
        Number(n-1)
Number(10)        

#from 1 to 5 
def fact(n):
    if n == 5:
        return 5
    else:
        return n*fact(n+1)
print(fact(1))

#from 5 to 1
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
for i in range(5):
    print(fib(i))
    

#score board
def Score_board(overs):
    l=[];start=1
    while start<=overs:
        balls=1
        while balls<=6:
            ball_score=input(f"enter over {start} ball:{balls}:")
            if ball_score=="wd" or ball_score=="nb":
                l.append(1)
                continue
            else:
                l.append(ball_score)
                balls+=1
        print(l)
        start+=1
    
Score_board(2)

#user define functions
def Length(x):
    count = 0
    for i in x:
        count+=1
    return count    


def Pavani(a):
    total = 0
    for i in a:
        total = total + i
    return total



#anomymous function
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

'''
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [j for i in a for j in i]

print(res)


overs = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4]]

balls = [ball for over in overs for ball in over]

print(len(balls))



































