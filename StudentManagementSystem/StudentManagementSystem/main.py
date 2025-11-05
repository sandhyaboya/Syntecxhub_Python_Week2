from student_manager import Student, StudentManager

def main():
    manager = StudentManager()
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            student = Student(sid, name, grade)
            manager.add_student(student)

        elif choice == "2":
            manager.list_students()

        elif choice == "3":
            sid = input("Enter ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
