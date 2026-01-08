# Large Python Application for Git & GitHub Experiment (VS Code)
# File name: student_management_system.py


students = {}

# Function to add a student
def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student already exists")
        return
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    students[sid] = {"name": name, "dept": dept}
    print("Student added successfully")

# Function to view all students
def view_students():
    if not students:
        print("No student records found")
        return
    print("\nStudent Records")
    for sid, details in students.items():
        print(f"ID: {sid}, Name: {details['name']}, Department: {details['dept']}")

# Function to update student details
def update_student():
    sid = input("Enter Student ID to update: ")
    if sid not in students:
        print("Student not found")
        return
    name = input("Enter new name: ")
    dept = input("Enter new department: ")
    students[sid]["name"] = name
    students[sid]["dept"] = dept
    print("Student details updated")

# Function to delete a student
def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully")
    else:
        print("Student not found")
        
def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        s = students[sid]
        print(f"ID: {sid}, Name: {s['name']}, Dept: {s['dept']}")
    else:
        print("Student not found")

# Main menu
def menu():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting application")
            break
        else:
            print("Invalid choice. Try again")

# Program execution
menu()
