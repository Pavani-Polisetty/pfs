#if Programs
#Write a program to check if a number is greater than 10.

n = int(input())
if n > 10:
    print("Greatest of 10")


#Write a program to check if a person is eligible to vote (age 18 or above).

age = int(input())
if age >=18:
    print("Eligible")


#Write a program to check if a number is positive.
number = int(input())
if number > 0:
    print("Positive")


#Write a program to check if a number is negative.

number = int(input())
if number < 0:
    print("Negative")



#if-else programs
#Write a program to check if a number is even or odd.
number = int(input())
if number%2 == 0:
    print("Even")
else:
    print("Odd")




#Write a program to check if a person is eligible for a driving license (age 18 or above).
age = int(input())
if age > 18:
    print("Eligible")
else:
    print("Not Eligible")




#Write a program to check if a number is positive or negative.

number = int(input())
if number > 0:
    print("Positive")
else:
    print("Negative")


#Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40).
marks = int(input())
if marks >=40:
    print("passed")
else:
    print("Failed")



#if-elif-else 
#Write a program to classify a number as positive, negative, or zero.
number =int(input())
if number > 0:
    print("Positive")
elif number <0:
    print("Negative")
else:
    print("Zero")



#Write a program to categorize a person’s age as a child (0-12),
#teenager (13-19), or adult (20+).
age = int(input())
if age >=0 and age <= 12:
    print("Child")
elif age >=13 and age <=19:
    print("Teenage")
else:
    print("Adult")

##Write a program to determine the grade of a student based on marks
##(A: 90+, B: 80+, C: 70+, D: 60+, Fail: <40).
marks = int(input())
if marks >= 90:
    print("GradeA")
elif marks >=80 and marks< 90:
    print("Grade B")
elif marks >=70 and marks < 80:
    print("Grade C")
elif marks >=60 and marks < 70:
    print("Grade D")
else:
    print("Fail")
 
#Nested if conditions
#A bank checks if a person is eligible for a loan based on their age and salary.
age = int(input())
if age > 20:
    salary = int(input())
    if salary >= 10000:
        print("Eligible for loan")
    else:
        print("Salary must be 10000")
else:
    print("age must be greater than 20")


#A student needs at least 35 marks to pass. If they score above 90, they get a scholarship.
marks = int(input())
if marks >=35:
    if marks >= 90:
        print("eligible for scholarship")
    else:
        print("Not eligible for scholarship")
else:
    print("Marks must be greater than 35")


#Order Discounts & Shipping Charges
amount = int(input())
if amount > 500:
    print("Free shipping")
else:
    print("shipping charge is ", amount+50)

#Banking & Finance (HDFC, ICICI, PayPal, Razorpay)
#Loan Eligibility Checking
salary = int(input())
cibil_score = int(input())
if salary > 50000 and cibil_score > 750:
    print("approve loan")
else:
    print("Reject loan")



#Ride-Sharing Services (Uber, Ola,rapido)
#Surge Pricing Logic
peak_hours = input()
high_demand = input()
if peak_hours == "Yes" and high_demand == "Yes":
    print("Apply surge pricing")
else:
    print("Normal fare")

               #OR

peak_hours = input()
high_demand = input()
if peak_hours == "Yes":
    if high_demand == "Yes":
        print("Apply surge pricing")
    else:
        print("Normal fare")
else:
    print("Normal fare")



#Food Delivery Services (Zomato, Swiggy, Uber Eats)
#Restaurant Order Availability
restaurant = input()
if restaurant == "Open" or restaurant == "open":
    print("Item available")
else:
    print("Item Not available")

#Streaming Services (Netflix, YouTube, Hotstar)
#Video Quality Adjustment
internet_speed = int(input())

if internet_speed > 10:
    print("quality - 108p")
elif internet_speed > 5:
    print("quality - 720p")
else:
    print("quality - 480")
    

#Scenario: A system checks if a user is eligible for a senior citizen discount
#(age ≥ 60).
#Write a program that takes a person's age as input and prints
#"Eligible for discount" if they are 60 or older.
age = int(input())
if age >= 60:
    print("Eligible for senior citizen")
    

#Scenario: A shopping site offers free shipping for orders above ₹500.
#Write a program that takes the total bill amount as input.If it's above ₹500,
#print "Free Shipping",otherwise print "Shipping Charges Applied".
total_bill_amount = int(input())
if total_bill_amount > 500:
    print("Free shipping")
else:
    print("Shipping Charges Applied")

##Scenario: A system classifies water usage based on liters used.
##Write a program that takes the number of liters used as input.
##If usage is less than 100 liters, print "Low usage".
##If usage is between 100 and 500 liters, print "Moderate usage".
##If usage is above 500 liters, print "High usage".

no_of_liters = int(input())
if no_of_liters < 100:
    print("Low usage")
elif no_of_liters > 100 and no_of_liters < 500:
    print("Moderate usage")
else:
    print("High usage")

#Scenario: A movie booking system checks age and ticket availability.
age = int(input())
if age >= 18:
    seats = input()
    if seats == "Available" or seats == "available":
        print("Booking Confirmed")
    else:
        print("Tickets Sold Out")
else:
    print("Not eligible for this movie")
'''
#string methods
#Replace all occurrences of "a" with "@" in a given string.
'''
name = input()
print(name.replace('a','@'))


#Write a program to print the first and last character of a given string.
string = input()
print(string[0])
print(string[-1])


#Write a program to convert a string to uppercase and lowercase.
name = input()
print(name.upper())
print(name.lower())

#Write a program to remove all spaces from a given string.
string = input()
print(string.strip())

#Check if the word "Python" exists in the given sentence.
sentence = input()
if "Python" in sentence:
    print("Exists")
else:
    print("Not Exists")

#Print the first three characters of a given string.
string = input()
print(string[0:3])


#Take two strings as input and merge them.
string1 = input()
string2 = input()
print(string1+string2)


#Write a program to check if a string contains only numbers.
string = input()
print(string.isdigit())


#Remove all occurrences of "e" from a string.
string = input()
string = string.replace("e", "")
print(string)


#Count how many times the letter 'o' appears in a given string.
string = input()
print(string.count('o'))


#Check if a username contains only letters and numbers
string = input()
print(string.isalnum())


#An email has "@" and ends with ".com".
string = input()
print('@' in string and string.endswith(".com"))


#Ensure a password contains at least 8 characters, a number, and a special
#character.
s = input()
print(len(s) >= 8 and any(c.isdigit() for c in s) and any(not c.isalnum() for c in s))

#Write a program to find the length of a given string without using len().
s = input()
count = 0
for i in s:
    count+=1
print(count)


#Write a Python program to reverse a given string.
string = input()
print(string[::-1])


#Count Vowels in a String
string = input()
count = 0
for i in string:
    if i in "aeiouAEIOU":
        count+=1
print(count)


#Count consonants in a string
string = input()
count = 0
for i in string:
    if i not in "aeiouAEIOU":
        count+=1
print(count)


#Print numbers from 1 to 10 using a for loop.
n=int(input())
for i in range(n):
    print(i)

#Print numbers from 10 to 1 using a while loop.
n=int(input())
i = n
while i>0:
    print(i)
    i-=1

#Print all even numbers from 1 to 20.
n = int(input())
for i in range(n):
    if i%2 == 0:
        print(i)

      
#Print the sum of the first 10 natural numbers
n = int(input())
sum = 0
for i in range(n):
    sum+=i
print(sum)


#Print the multiplication table of a given number.
n = int(input())
for i in range(1,11):
    print(f"{n}*{i} ={n*i}")


#Find the factorial of a given number using a while loop.
n = int(input())
fact = 1
for i in range(n):
    fact=fact*n
    n=n-1
print(fact)


#Check if a number is prime or not.
n = int(input())
if n <= 1:
    print("Not Prime")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")


#Find the sum of digits of a given number.
number = int(input())
sum = 0
while number>0:
    digit=number%10
    sum+=digit
    number = number // 10
print(sum)


#Print all odd numbers from 1 to 50.
number = int(input())
for i in range(number):
    if i%2!=0:
        print(i)


#Find the largest number in a list using a loop
numbers = list(map(int, input().split()))
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)


#Print all numbers from 1 to 100 that are divisible by 5.
for i in range(101):
    if i % 5 == 0:
        print(i)

#tuple programs
#Write a program to create a tuple containing integers, strings, and floats.
#Print the tuple.
my_tuple = (10, 20, "Python", "Hello", 3.14, 5.6)
print(my_tuple)

#Given the tuple t = (10, 20, 30, 40, 50), write a program to print the first
#and last elements using indexing.
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])


#Write a program to slice a tuple t = (1, 2, 3, 4, 5) and print elements
#from index 1 to 3.
t = (1, 2, 3, 4, 5)
print(t[1:4])

#Given a tuple t = (1, 2, (3, 4), 5), write a program to access the second
#element of the nested tuple
t = (1, 2, (3, 4), 5)
print(t[2][1])


#Write a program to find how many times a specific element appears in a
#tuple t = (1, 2, 3, 1, 4, 1).

t = (1, 2, 3, 1, 4, 1)

n = int(input())
print(t.count(n))

         #OR
t = (1, 2, 3, 1, 4, 1)

for i in t:
    print(i, ":", t.count(i))


#Write a program to find the index of a specific element in the tuple
#t = ("apple", "banana", "cherry").
t = ("apple", "banana", "cherry")
print(t.index("apple"))

#Write a program to concatenate two tuples and print the result.For example,
#t1 = (1, 2, 3) and t2 = (4, 5, 6).

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1+t2
print(t3)

#Write a program to multiply a tuple by an integer. For example, multiply the
#tuple t = (1, 2) by 3.
t = (1, 2)
n = int(input())
result = t * n
print(result)


#Write a program to find the length of a given tuple.
t = ("apple", "banana", "cherry")
print(len(t))


#Write a program to check if an element exists in a given tuple.
t = (1, 2, 3, 1, 4, 1)
n = int(input())
if n in t:
    print("exits")


#Write a program to delete a tuple after it has been created and print a message.
t = (1, 2, 3, 1, 4, 1)
del t
print("tuple deleted successfully")

#dictionary programs
#Create and Print a Dictionary
my_dict = {"name": "Pavani","age": 21,"city": "Eluru"}
print(my_dict)


#Access a Value Using Key
my_dict = {"name": "Pavani","age": 21,"city": "Eluru"}
key = input()
print(my_dict[key])


#Add a New Key-Value Pair same for update also
my_dict = {"name": "Pavani","age": 21,"city": "Eluru"}
key = input()
value = input()
my_dict[key] = value
print(my_dict)


#Delete a Key-Value Pair
my_dict = {"name": "Pavani","age": 21,"city": "Eluru"}
key = input()
del my_dict[key]
print(my_dict)

#word Pattern
word = input().upper()

for i in range(7):
    for ch in word:
        for j in range(5):

            if ch == 'A':
                if (i == 0 and j in (1, 2, 3)) or \
                   (i in (1, 5) and j in (0, 4)) or \
                   (i in (2, 3, 4) and j in (0, 1, 2, 3, 4)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'B':
                if j == 0 or (i in (0, 3, 6) and j < 4) or \
                   (j == 4 and i in (1, 2, 4, 5)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'C':
                if i in (0, 6) and j > 0 or j == 0 and i not in (0, 6) or \
                   i == 1 and j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'D':
                if j == 0 or (i in (0, 6) and j < 4) or \
                   (j == 4 and i not in (0, 6)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'E':
                if i in (0, 3, 6) or j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'F':
                if i == 0 or i == 3 or j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'G':
                if i == 0 and j > 0 or i == 6 and j > 0 or \
                   j == 0 and i not in (0, 6) or \
                   i == 3 and j >= 2 or j == 4 and i >= 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'H':
                if j == 0 or j == 4 or i == 3:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'I':
                if i in (0, 6) or j == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'J':
                if i == 0 or j == 2 or i == 6 and j < 3 or \
                   i == 5 and j == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'K':
                if j == 0 or (i + j == 4) or (i - j == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'L':
                if j == 0 or i == 6:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'M':
                if j == 0 or j == 4 or (i == j and i < 3) or \
                   (i + j == 4 and i < 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'N':
                if j == 0 or j == 4 or i == j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'O':
                if (i in (0, 6) and j in (1, 2, 3)) or \
                   (j in (0, 4) and i not in (0, 6)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'P':
                if j == 0 or (i in (0, 3) and j < 4) or \
                   (j == 4 and i in (1, 2)):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'Q':
                if (i in (0, 5) and j in (1, 2, 3)) or \
                   (j in (0, 4) and i in (1, 2, 3, 4)) or \
                   (i == 6 and j == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'R':
                if j == 0 or (i in (0, 3) and j < 4) or \
                   (j == 4 and i in (1, 2)) or \
                   (i == 4 and j == 2) or (i == 5 and j == 3) or \
                   (i == 6 and j == 4):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'S':
                if i in (0, 3, 6) or i in (1, 2) and j == 0 or \
                   i in (4, 5) and j == 4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'T':
                if i == 0 or j == 2:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'U':
                if j in (0, 4) and i < 6 or i == 6 and j in (1, 2, 3):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'V':
                if (j == 0 and i < 4) or (j == 4 and i < 4) or \
                   (i == 4 and j in (1, 3)) or \
                   (i == 5 and j == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'W':
                if j == 0 or j == 4 or \
                   (i == 4 and j in (1, 3)) or (i == 5 and j == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'X':
                if i == j or i + j == 4:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'Y':
                if (i < 3 and j in (0, 4) and i == j) or \
                   (i < 3 and i + j == 4) or (i >= 3 and j == 2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            elif ch == 'Z':
                if i in (0, 6) or i + j == 6:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")

            else:
                print(" ", end=" ")

        print(" ", end=" ")
    print()


'''
* * * *     * 
      *     * 
      *     * 
* * * * * * * 
*     *       
*     *       
*     * * * * 
'''
n = int(input()

for i in range(n):
    for j in range(n):
        if i == n//2 or j==n//2 or \
        (i == 0 and j<n//2) or (i == n-1 and j>n//2) or \
        (j == 0  and i>n//2) or (j == n-1 and i<n//2):
            print("*",end = " ")
        else:
            print(" ", end=" ")
    print()






