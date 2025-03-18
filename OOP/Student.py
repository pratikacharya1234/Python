#OOP
#class -blueprint of an object
class Student:
    school_name = "Weber State University"
    all_students = [] #class variable - shared by all instances of the class
    #constructor initializer the object
    #attributes - property
    def __init__(self, first_name, last_name, grade, student_id=None):
        
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + "@mail.weber.edu"
        self.student_id = self.format_student_id(student_id)

        #add student to the list of all students
        Student.all_students.append(self)

    @classmethod
    def from_full_name(cls, full_name, grade, student_id):
         first_name, last_name= full_name.split()
         return cls(first_name, last_name, grade, student_id)


    def print_student_data(self):
            print(f"\tStudent INFO \n",
                  f"\tName: {self.first_name} {self.last_name}\n", 
                  f"\tStudentID {self.student_id}\n",
                  f"\temail: {self.email}")
            
    #@static method in python is  a decorator that defins a method
    # that belong to a class rather than the instance, unlike 
    # @classmethod it doesn't use cls
    @staticmethod
    def format_student_id(student_id):
         #format student ID with a leading "WSU" prefix it exists
         return f"WSU-{student_id}" if student_id else "No ID assigned"




  # class method to get all students          
    def get_all_students(cls):
        return cls.all_students

    #method - behavior
    @classmethod
    def change_grade(self, new_grade_level):
        self.grade = new_grade_level

    def __str__(self):
        #The __str__ method provides a user_friendly string representsation of the object.
        # This is called when print() the instance of the class.
        return (f"Student: {self.first_name}, {self.last_name} ,Grade: {self.grade},Student ID: {self.student_id}, Email: {self.email}, School: {self.school_name}.")

#first student object
#Create an Instance of the object
waldo = Student.from_full_name("Waldo Wildcat", "Sophomore",4567)
jane = Student("Jane", "Doe", "Senior",1233)
john = Student("John", "Doe", "Freshman",1234)


#print
waldo.print_student_data()
jane.print_student_data()
john.print_student_data()
#change grade
waldo.change_grade("Senior")
jane.change_grade("Senior")
john.change_grade("Senior")
# print again
waldo.print_student_data()
jane.print_student_data()
john.print_student_data()

# print all students
for student in Student.all_students:
    print(student)

# # print all students
# students =  Student.get_all_students()
# for student in students:
#      student.print_student_data()
