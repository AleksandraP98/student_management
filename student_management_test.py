import unittest
import os
from student_management import Student, save_students_to_file, load_students_from_file


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.students = [
            Student(1, "Alice", 19, "Freshman", ["Math", "History"]),
            Student(2, "Bob", 22, "Sophomore", ["English", "Science"])
        ]
        self.test_file = "test_students.json"

    def test_student_initialization(self):
        student = Student(3, "Charlie", 19, "Junior", ["Biology", "Chemistry"])
        self.assertEqual(student.student_id, 3)
        self.assertEqual(student.name, "Charlie")
        self.assertEqual(student.age, 19)
        self.assertEqual(student.grade, "Junior")
        self.assertEqual(student.subjects, ["Biology", "Chemistry"])

    def test_update_student_info(self):
        student = self.students[0]
        student.update_student_info("name", "Alice Cooper")
        self.assertEqual(student.name, "Alice Cooper")

        student.update_student_info("age", "21")
        self.assertEqual(student.age, 21)

        student.update_student_info("grade", "Senior")
        self.assertEqual(student.grade, "Senior")

        student.update_student_info("subjects", "Physics, Art")
        self.assertEqual(student.subjects, ["Physics", "Art"])

    def test_save_students_to_file(self):
        save_students_to_file(self.students, self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, "r") as file:
            data = file.read()
            self.assertIn("Alice", data)
            self.assertIn("Bob", data)

    def test_load_students_from_file(self):
        save_students_to_file(self.students, self.test_file)
        loaded_students = load_students_from_file(self.test_file)

        self.assertEqual(len(loaded_students), 2)
        self.assertEqual(loaded_students[0].name, "Alice")
        self.assertEqual(loaded_students[0].grade, "Freshman")

    def test_add_student(self):
        new_student = Student(3, "Charlie", 19, "Junior", ["Art", "History"])
        self.students.append(new_student)

        self.assertEqual(len(self.students), 3)
        self.assertEqual(self.students[2].name, "Charlie")

    def test_delete_student(self):
        student_to_remove = self.students[0]
        self.students.remove(student_to_remove)

        self.assertEqual(len(self.students), 1)
        self.assertNotIn(student_to_remove, self.students)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main()
