'''3

#nested for loops
for i in range(5):
    for j in range(5):
        print(j,end = " ")#when we place end the loop will changes like a row
    print()    



n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end = " ")
    print()    


n= int(input())
for i in  range(n-1):
    for j in range(n-1):
        print("*",end = " ")
    print()

'''

'''
000
111
222
when column value is changed outer loop value must print
'''
##n= int(input())
##for i in  range(n):
##    for j in range(n):
##        print(i,end = " ")
##    print()


'''
for i in range(2,0,-1):
  for j in range(3,0,-1):
    print(i,end=" ")
  print()

'''

##n = int(input())
##upto = int(input())
##for i in range(n,upto):
##    print(f"{n}*{n}={n*i}")





'''
p
p a
p a v
p a v a
p a v a n
p a v a n i
'''
##s = input()
##for i in range(len(s)):
##    for j in range(i+1):
##        print(s[j],end=" ")
##    print()


#vowels and consonants length

##s = input()
##vowels = "aeiouAEIOU"
##v = ""
##c = ""
##for i in s:
##    if i in vowels:
##        v += i
##    else:
##        c +=i
##print(v, "-",len(v))
##print(c, "-",len(c))


'''
leap years - [2000, 2004]
Non leap years 4- [2003, 1990]
'''
##
##years = list(map(int, input().split()))
##
##leap_years = []
##non_leap_years = []
##
##for i in years:
##    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
##        leap_years.append(i)
##    else:
##        non_leap_years.append(i)
##        
##print("leap years -",  leap_years)
##print("Non leap years -",  non_leap_years)

*        *
  *    * 
    *
  *   *
*       *
  

##n = int(input())
##for i in range(n):
##    for j in range(n):
##        if i == j or i+j == n-1:
##            print("*",end=" ")
##        else:
##            print(" ",end= " ")
##    print()

*       * 
* *   * * 
*   *   * 
*       * 
*       * 

##n = int(input())
##for i in range(n):
##    for j in range(n):
##        if j == 0 or j == n-1 or  (i == j and i<=n//2) or (i+j == n-1 and i<=n//2):
##            print("*",end = "")
##        else:
##            print(" ",end=" ")
##    print()        



for i in range(5):
    for j in range(5+4):
        if i==j or i+j==8:
            print("*",end="")
        else:
            print(" ",end="")
    print()



#factorial
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(fact)


#palindrome
n = int(input())
temp = n
rev = 0

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")







































  
