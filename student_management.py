import json

class Student:
    def __init__(self, student_id, name, age, grade, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
    
    def update_student_info(self, attribute, new_value):
        if attribute == "name":
            self.name = new_value
        elif attribute == "age":
            self.age = int(new_value)
        elif attribute == "grade":
            self.grade = new_value
        elif attribute == "subjects":
            self.subjects = new_value.split(", ")  
        else:
            print("Invalid attribute.")
    
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)}")

def save_students_to_file(students, filename="students.txt"):
    try:
        with open(filename, 'w') as file:
            student_data = [student.__dict__ for student in students]  
            json.dump(student_data, file, indent=4)
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_students_from_file(filename="students.txt"):
    students = []
    try:
        with open(filename, 'r') as file:
            student_data = json.load(file)
            for student_dict in student_data:
                students.append(Student(**student_dict))  
    except Exception as e:
        print(f"Error loading from file: {e}")
    return students

def main_menu():
    print("\nStudent Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update student information")
    print("4. Delete a student")
    print("5. Save and Exit")
    
    choice = input("Choose an option: ")
    return choice

def add_student(students):
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    subjects = input("Enter subjects (comma-separated): ").split(", ")
    
    for student in students:
        if student.student_id == student_id:
            print("Error: Student ID already exists.")
            return
    
    new_student = Student(student_id, name, age, grade, subjects)
    students.append(new_student)

def view_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        student.display()

def update_student(students):
    student_id = int(input("Enter student ID to update: "))
    student = next((s for s in students if s.student_id == student_id), None)
    
    if student:
        print("What do you want to update? (name, age, grade, subjects)")
        attribute = input("Choose an attribute: ")
        new_value = input(f"Enter new value for {attribute}: ")
        student.update_student_info(attribute, new_value)
    else:
        print("Student ID not found.")

def delete_student(students):
    student_id = int(input("Enter student ID to delete: "))
    student = next((s for s in students if s.student_id == student_id), None)
    
    if student:
        students.remove(student)
        print(f"Student with ID {student_id} removed.")
    else:
        print("Student ID not found.")

def main():
    students = load_students_from_file()
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_students_to_file(students)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
