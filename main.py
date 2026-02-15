import json
import os

FILE_NAME = "students.json"
students = []


def load_data():
    global students
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            students = []
    else:
        students = []


def save_data():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)
    print("Data saved.\n")


def calculate_grade(avg):
    if avg >= 75:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 50:
        return "C"
    return "F"


def add_student():
    roll = input("Roll No: ").strip()
    name = input("Name: ").strip()

    # Basic validation
    if not roll or not name:
        print("Roll and name cannot be empty.\n")
        return

    if any(s["roll"] == roll for s in students):
        print("This roll number already exists.\n")
        return

    marks_str = input("Enter marks (space separated): ").strip()
    if not marks_str:
        print("Marks cannot be empty.\n")
        return

    try:
        marks = [int(x) for x in marks_str.split()]
        if any(m < 0 for m in marks):
            print("Marks cannot be negative.\n")
            return
    except ValueError:
        print("Invalid marks. Enter integers only.\n")
        return

    total = sum(marks)
    avg = round(total / len(marks), 2)
    grade = calculate_grade(avg)

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "average": avg,
        "grade": grade
    })

    print("Student added successfully.\n")


def display_students():
    if not students:
        print("No records found.\n")
        return

    print("\nRoll | Name | Marks | Total | Average | Grade")
    print("-" * 55)
    for s in students:
        marks_str = " ".join(map(str, s["marks"]))
        print(f"{s['roll']} | {s['name']} | {marks_str} | {s['total']} | {s['average']:.2f} | {s['grade']}")
    print()


def search_student():
    roll = input("Enter roll number to search: ").strip()
    for s in students:
        if s["roll"] == roll:
            print("\nRecord Found:")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Total: {s['total']}")
            print(f"Average: {s['average']:.2f}")
            print(f"Grade: {s['grade']}\n")
            return
    print("No student found with that roll number.\n")


def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    for i, s in enumerate(students):
        if s["roll"] == roll:
            students.pop(i)
            print("Student deleted.\n")
            return
    print("No student found with that roll number.\n")


def menu():
    load_data()

    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save & Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_data()
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    menu()
