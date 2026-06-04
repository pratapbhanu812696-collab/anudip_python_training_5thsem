# Student Result Management System in grade A+,B+,B, C+, C, D, F
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks >= 80:
            return 'B+'
        elif self.marks >= 70:
            return 'B'
        elif self.marks >= 60:
            return 'C+'
        elif self.marks >= 50:
            return 'C'
        elif self.marks >= 40:
            return 'D'
        else:
            return 'F'

    def display_result(self):
        grade = self.calculate_grade()
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {grade}")
# Example usage
student1 = Student("Alice", "101", 95)
student2 = Student("Bob", "102", 85)
student3 = Student("Charlie", "103", 75)
student4 = Student("David", "104", 65)
student5 = Student("Eve", "105", 55)
student6 = Student("Frank", "106", 35)
student1.display_result()
print()
student2.display_result()
print()
student3.display_result()
print()
student4.display_result()
print()
student5.display_result()
print()
student6.display_result()
print()



