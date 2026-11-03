import json
import os
def find_db():
    if not os.path.exists("student_details.json"):
        with open("student_details.json","w")as file:
            json.dump({},file,indent=4)


detailes="student_details.json"

def load_data():
    with open(detailes, "r") as file:
        user=json.load(file)
        return user

def add_data(user):
    with open(detailes, "w") as file:
        json.dump(user,file,indent=4)

def add_student(students):
    n=int(input("enter the number of students"))
    for i in range(n):
        roll_no = input("enter a roll number: ")
        if roll_no in students:
            print("student already registered")
        else:
            score = {}
            name = input("enter your name: ")
            branch = input("enter your branch: ")
            print("Enter your academic records")
            n = int(input("enter number no subjet: "))
            print("enter your subject name and marks out of 100")
            for a in range(n):
                subject = input("enter subject: ")
                marks = float(input("enter marks: "))
                score[subject] = marks

            students[roll_no] = {"Name": name, "Branch": branch, "Academic_score": score}
            add_data(students)
        print("student details added")

def display_students(students):

    if not students:
        print("No students registered yet.")
        return

    for roll, details in students.items():

        print("\n--------------------------")
        print("Roll Number:", roll)
        print("Name:", details["Name"])
        print("Branch:", details["Branch"])

        print("Academic score:")
        for r,v in details["Academic_score"].items():
            print(r,":",v)


def calculate_result(students):
    total = 0
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found!")
        return
    s = students[roll]["Academic_score"]

    if len(s) == 0:
        print("No marks available.")
        return

    total_marks=sum(s.values())
    average = total_marks / len(s)


    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n===== STUDENT RESULT =====")
    print("Name:", students[roll]["Name"])
    print("Branch:", students[roll]["Branch"])
    print("Academic score:", students[roll]["Academic_score"])
    print("Average:", round(average, 2))
    print("Grade:", grade)

def search_student(students):

    roll = input("Enter roll number to search: ")

    if roll in students:
        print("Student Found!")
        print("Name:", students[roll]["Name"])
        print("Branch:", students[roll]["Branch"])
        print("Academic score:", students[roll]["Academic_score"])
    else:
        print("Student not found!")

def main():
    find_db()
    #menu of functions
    while True:
        students=load_data()
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Student Result")
        print("4. Search Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_result(students)
        elif choice == "4":
            search_student(students)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()