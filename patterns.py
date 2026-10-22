'''
0 *
1 * *
2 * * *
3 * * * *
'''
##n = int(input())
##for i  in range(n):
##    for j in range(i+1):
##        print("*",end= "")
##    print()    


'''
4 *
3 * *
2 * * *
1 * * * *
'''
##n = int(input())
##for i  in range(n):
##    for j in range(n-i+1):
##        print("*",end= "")
##    print()
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
#in for while loop 
##n = int(input())
##for i  in range(n):
##    for spaces in range(n-i-1):
##        print(" ",end= "")
##    for stars in range(i+1):
##        print("*",end= "")    
##    print()



#in while loop
##n = int(input())
##
##i = 0
##while i < n:
##    spaces = 0
##    while spaces < n - i - 1:
##        print(" ", end="")
##        spaces += 1
##
##    stars = 0
##    while stars < i + 1:
##        print("*", end="")
##        stars += 1
##
##    print()
##    i += 1




##for i in range(2,0,-1):
##  for j in range(3,0,-1):
##    print(i,end=" ")
##  print()




##n = int(input())
##for i  in range(n):
##    for j in range(i+1,0,-1):
##        print(j,end= "")
##    print() 




'''
      1
    1 2
  1 2 3
1 2 3 4
'''

##n = int(input())
##
##for i in range(n):
##    for spaces in range(n-i-1):
##        print(" ", end=" ")
##    for k in range(i+1):
##        print(k+1, end=" ")
##    print()

'''
4
4 3
4 3 2
4 3 2 1
'''

##n = int(input())
##
##for i in range(n):
##    for j in range(i + 1):
##        print(n - j, end=" ")
##    print() 

##'''
##A
##B B
##C C C
##D D D D
##'''
##n = int(input())
##for i in range(65,n+4):
##    for j in range(65,i+1):
##        print(chr(i),end=" ")
##    print()
##'''
##D
##D C
##D C B
##D C B A
##'''
##for i in range(68,64,-1):
##    for j in range(68,i-1,-1):
##        print(chr(j),end=" ")
##    print()



##n=int(input())
##for i in range(n):
##    for j in range(n,n-i-1,-1):
##        print(chr(j),end=" ")
##    print()

'''
* * * * *
*       *   
*       *
*       *
*       *
* * * * *  

'''
##for i in range(5):
##    for j in range(5):
##        if i==0 or j==0 or i==4 or j==4:
##            print("*",end=" ")
##        else:
##            print(" ",end=" ")
##    print()

'''
p
p a
p a v
p a v a
p a v a n
p a v a n i
'''
s = input()
for i in range(i,len(s)):
    for j in range(i+1):
        print(s[j],end=" ")
    print()

'''
p y t h o n
y t h o n
t h o n
h o n
o n
n
'''
s = input()

for i in range(len(s)):
    for j in range(i, len(s)):
        print(s[j], end=" ")
    print()






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




##
##s = input()
##vowels = "aeiouAEIOU"
##v = ""
##c = ""
##
##for ch in s:
##    if ch in vowels:
##        v += ch
##    else:
##        c += ch
##
##print(v, "-", len(v))
##print(c, "-", len(c))

##years = list(map(int,input().split()))
##leap_years = []
##non_leap_years = []
##for i in years:
##    if years % 400 == 0 or (years% 4 == 0 and years % 100 != 0):
##        leap_years.append(i)
##    else:
##        non_leap_year.append(i)
##print("leap years -",  leap_years)
##print("Non leap years -",  non_leap_years)
##
##
##
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
##print(*leap_years, "-", len(leap_years))
##print(*non_leap_years, "-", len(non_leap_years))
##
##'''
##* * * * *
##    *
##    *
##    *
##    *
##* * *
##'''
##
####n = int(input())
####for i in range(n):
####    for j in range(n):
####        if i == 0 or (i == 4 and j<=n//2) or j == n//2:
####            print("*",end="")
####    print()
##
##
##
####------------.|.------------
####---------.|..|..|.---------
####------.|..|..|..|..|.------
####---.|..|..|..|..|..|..|.---
####----------WELCOME----------
####---.|..|..|..|..|..|..|.---
####------.|..|..|..|..|.------
####---------.|..|..|.---------
####------------.|.------------
##n,m=map(int,input().split())
##for i in range(1,n,2):
##    symbol=".|."
##    print((symbol*i).center(m,"-")) 
##print("WELCOME".center(m,"-"))
##
##for j in range(n-2,0,-2):
##    symbol=".|."
##    print((symbol*j).center(m,"-"))


1010101
0000000
1010101
0000000
1010101
0000000
1010101
n = int(input())
for i in  range(n):
    for j in range(n):
        if i%2==0:
            print(1,end = "")
        else:
            print(0,end = "")
            

i=0
while i<5:
    j=0
    while j<5:
        if i%2==0 and j%2==0:
            print(1,end="")
        else:
            print("0",end="")
        j+=1
    print()
    i+=1

#factorial 1
n=5;fact=1
while n>0:
    fact*=n
    n-=1
print(fact)

#factorial 2
i=1
n=5
fact=1
while i<=n:
    print(i)
    fact*=i
    i+=1
print(fact)




#palindrome
n=input()
rev=n[::-1]
if n==rev:
    print("palidrome")
else:
    print("not")


#Palindrome
n=121;rev=0
temp=n
while n>0:
    last=n%10
    n=n//10
    rev=rev10+last  #rev=10+last

if rev==temp:
    print("plaidnorme")
else:
    print("not")



s="abccaaaa"
d={}
for i in range(len(s)):
    if s[i] in d:
        d[s[i]]+=1
    else:
        d[s[i]]=1
print(d)


d={"pavani":600,"sravya":400,"maheswari":600,"ram":500}
highest=0
for key,value in d.items():
    if value>=highest:
        highest=value
        print(key)


























































