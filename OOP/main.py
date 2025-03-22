#import the Student class from the Student module
from Student import Student
from gradudate_student import GraduateStudent

#first student object
#Create an Instance of the object
waldo = Student.from_full_name("Waldo Wildcat", "Sophomore",4567)
jane = Student("Jane", "Doe", "Senior",1233)
john = GraduateStudent("John", "Doe", "Freshman",)


# print all students
for student in Student.all_students:
    print(student)