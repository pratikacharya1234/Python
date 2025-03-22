#graduate_student is a child of the student class
from Student import Student

class GraduateStudent(Student):
    
    def __init__(self, first_name, last_name, grade, student_id = None, degree_program=None):
        super().__init__(first_name, last_name, grade, student_id)
        self.degree_program = degree_program

    def print_student_data(self):
        super().print_student_data()
        print(f"GRADUATE STUDENT:{self.first_name}, {self.last_name}, \tDegree Program: {self.degree_program}")