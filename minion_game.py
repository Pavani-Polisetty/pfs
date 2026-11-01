#minion game

def minion_game(string):
    vowels = "AEIOU"

    kevin = 0
    stuart = 0

    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


minion_game(input().upper())



#Reeborg's world!

def game(n):
    for i in range(4):
        for j in range(n-1):
            if front_is_clear():
                move()
        turn_left()

n = 10
game(n)
