import json

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student):
        if any(s["id"] == student.student_id for s in self.students):
            print("❌ Student ID already exists!")
            return
        self.students.append({"id": student.student_id, "name": student.name, "grade": student.grade})
        self.save_students()
        print("✅ Student added successfully!")

    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\n📋 Student Records:")
        for s in self.students:
            print(f"ID: {s['id']} | Name: {s['name']} | Grade: {s['grade']}")

    def delete_student(self, student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s["id"] != student_id]
        if len(self.students) < initial_count:
            self.save_students()
            print("🗑️ Student deleted successfully!")
        else:
            print("❌ Student ID not found!")
