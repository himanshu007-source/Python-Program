# Student Management System

students = {}


def add_student():
    roll = input("Enter roll number: ")

    if roll in students:
        print("Error: Roll number already exists!")
        return

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))

        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            return

        marks.append(mark)

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def display_students():
    if not students:
        print("No students registered yet.")
        return

    for roll, details in students.items():
        print("\n--------------------------")
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("Marks:", details["marks"])


def calculate_result():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found!")
        return

    marks = students[roll]["marks"]

    total = sum(marks)
    average = total / len(marks)

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
    print("Name:", students[roll]["name"])
    print("Total Marks:", total, "/ 300")
    print("Average:", round(average, 2))
    print("Grade:", grade)


def search_student():
    roll = input("Enter roll number to search: ")

    if roll in students:
        print("Student Found!")
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found!")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Calculate Student Result")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            calculate_result()

        elif choice == "4":
            search_student()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()