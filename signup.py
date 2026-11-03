import json
user={}

def add_data():
    with open("data.json", "w") as file:
        json.dump(user, file, indent=4)


while True:
    print("Welcome to the login and singup page")
    print("1. for sign up")
    print("2. for login")
    print("3. for exist")
    a = int(input("enter your choice: "))
    if a == 1:

        id = input("create your id: ")
        if id in user:
            print("Id already exists")
        else:
            password = input("create your password: ")
            p2 = input("confirm your password: ")
            if password == p2:
                user[id] = password
                add_data()
                print("signup successful")


            else:
                print("password not match")
                print("try again")


    elif a == 2:

        id = input("enter your id: ")
        if id in user:

            password = input("enter your password: ")
            if password == user[id]:
                print("Login successful")
            else:
                print("invalid password")
                print("try again")
        else:
            print("invalid id")
            print("sign up")
    elif a == 3:
        break
    else:
        print("invalid option")