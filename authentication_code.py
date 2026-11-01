#Authentication
'''
def Register():
    username = input("Enter username: ")

    if len(username) >= 2 and len(username) <= 12:
        password = input("Enter password: ")

        if len(password) >= 6 and len(password) <= 10:
            print("Registration successful")
            return username, password
        else:
            print("Password must be 6-10 characters")
            return None, None
    else:
        print("Username must be 2-12 characters")
        return None, None


def Login(reg_username, reg_password):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == reg_username and password == reg_password:
        print("Login successful")
    else:
        print("Invalid username or password")


username, password = Register()

if username is not None:
    Login(username, password)

'''
def login():
    id = input()
    password = int(input())
    if (password)==6:
        while


    










































