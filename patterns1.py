'''
      1
    1 2
  1 2 3
1 2 3 4
'''

n = int(input())

for i in range(n):
    for spaces in range(n-i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print(k+1, end=" ")
    print()

'''
4
4 3
4 3 2
4 3 2 1
'''

n = int(input())

for i in range(n):
    for j in range(i + 1):
        print(n - j, end=" ")
    print()    
