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






n = int(input())

for i in range(n):
    for spaces in range(n-i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print(k+1, end=" ")
    print()













































































