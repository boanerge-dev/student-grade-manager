students = []

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ")
    try:
        score = float(input("Enter student score (0-100): "))
        grade = calculate_grade(score)
        students.append({'name': name, 'score': score, 'grade': grade})
        print(f"{name} added with grade {grade}.")
    except ValueError:
        print("Invalid score. Please enter a number.")

def view_students():
    if not students:
        print("No students added yet.")
    else:
        print("\n--- Student Grades ---")
        for s in students:
            print(f"Name: {s['name']} | Score: {s['score']} | Grade: {s['grade']}")

def show_menu():
    print("\n==== STUDENT GRADE MANAGER ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
