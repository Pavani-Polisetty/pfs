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

n = int(input())
upto = int(input())
for iin range(n,upto):
    print(f"{n}*{n}={n*i}")














































  
