#conditions
##if condition:
##    statements

'''
username = input()
password = input()
if username == "pavani" and password == '123':
    print("credentials available")
else:
    print("wrong credentials")



n = int(input())
if n%2 == 0:
    print("even")

else:
    print("odd")
    



n = int(input())
if n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")
elif n%2==0:
    print("even")
else:
    print("not divisible by 3 and 5")


n=int(input())
if n%3==0:
    print("fizz")
if n%5==0:
    print("buzz")
if n%3==0 and n%5==0:
    print("fizz buzz")
else:
    print("normal numeber")


    

n=int(input())
if n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")
elif n%3==0 and n%5==0:
    print("fizz buzz")
else:
    print("normal numeber")





n=int(input())
if n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")
if n%3==0 and n%5==0:
    print("fizz buzz")
else:
    print("normal numeber")




n=int(input())
if n%3==0 and n%5==0:
    print("fizz buzz")
elif n%3==0:
    print("fizz")
elif n%5==0:
    print("buzz")

else:
    print("normal numeber")




n=input()
if n.isupper():
    print("Allow")
else:
    print("No")



n = input()
if n.isupper():
    print(n.lower())
else:
    print(n.upper())

n = input()
print(n.swapcase())




n = int(input())
a = n+10
if a%2==0:
    print("Even")

else:
    print("Odd")




year = int(input())

if year % 400 == 0 or (year% 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not Leap year")


#cars needed

customers = int(input())

if customers%4==0:
    print(customers//4)
else:
    print(customers//4+1)
    


n = int(input())

if n == 0:
    print("Zero")

elif n>0:
    print("Positive")

else:
    print("negative")



password = input()
if len(password) == 8:
    print("Weak")
elif len(password)>8 and len(password)<16:
    print("Good")
elif len(password)>15 and len(password)<20:
    print("excellent")
elif len(password)>20:
    print("hard to remember")
else:
    print("Not valid")
pavan




username = input()
if username == "Pavani":
    password = input()
    if password == "123":
        print("Login")
    else:
        print("Password is not")

else:
    print("worng username")



#nested conditios for finding student eligibility

year = int(input())
if year == 4:
    marks = int(input())
    if marks>=81 and marks<=100:
        backlogs = int(input())
        if backlogs == 0:
            print("allowed for special training")
        else:
            print("backlogs must be zero")
    else:
        print("marks must be greater than 81")  
else:
    print("must be in 4th year")





year = int(input())
if year == 4:
    marks = int(input())
    if marks>=81 and marks<=100:
        backlogs = int(input())
        if backlogs != 0:
            if backlogs>=1 and backlogs<=3:
                pay = int(input())
                if pay == "yes":
                    print("eligible for training ")
                else:
                    print("must need to pay")
            elif backlogs>3:
                pay = int(input())
                if pay == "yes":
                    print("eligible for training")
                else:
                    print("must need to pay 10k")
        else:
            print("eligible")
    else:
        print("marks must be greater than 81")  
else:
    print("must be in 4th year")



#sir problem
year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input("enter marks:"))
    
    if marks>80 and marks<=100:
        backlogs=int(input("enter bakclogs:"))
        
        if backlogs!=0:
            if backlogs>=1 and backlogs<=3:
                
                pay=input("you have to pay 5000 extra: [yes (or) no]:")
                if pay=="yes":
                    print("eligible for training")
                else:
                    print("must need to pay")

            elif backlogs>3:
                
                pay=input("you have to pay 10k [yes (or) no]:")
                if pay=="yes":
                    print("eligible for trainig")
                else:
                    print("must need to pay 10k")
                    
            
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")


'''


















































