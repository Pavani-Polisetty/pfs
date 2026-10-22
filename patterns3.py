'''
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
n = 7

for i in range(n):
    for j in range(n):
        if i == n//2 or j==n//2 or \
        (i == 0 and j<n//2) or (i == n-1 and j>n//2) or \
        (j == 0  and i>n//2) or (j == n-1 and i<n//2):
            print("*",end = " ")
        else:
            print(" ", end=" ")
    print()
