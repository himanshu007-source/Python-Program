import json
import os
def find_db():
    if not os.path.exists("user_details.json"):
        with open("user_details.json","w")as file:
            json.dump({},file,indent=4)


detailes="user_details.json"

def load_data():
    with open(detailes, "r") as file:
        user=json.load(file)
        return user

def add_data(user):
    with open(detailes, "w") as file:
        json.dump(user,file,indent=4)

def signup_page(user):
    id = input("create your id: ")
    if id in user:
        print("Id already exists")
    else:
        password = input("create your password: ")
        p2 = input("confirm your password: ")
        if password == p2:
            user[id] = password
            add_data(user)
            print("signup successful")


        else:
            print("password not match")
            print("try again")

def login_page(user):
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


def main():
    find_db()
    while True:
        user = load_data()
        print("Welcome to the login and singup page")
        print("1. for sign up")
        print("2. for login")
        print("3. for exist")
        a = int(input("enter your choice: "))
        if a == 1:
            signup_page(user)
        elif a == 2:
            login_page(user)
        elif a == 3:
            break
        else:
            print("invalid option")

main()
