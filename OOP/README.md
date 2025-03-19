# Student Class

A Python class for managing student information at Weber State University.

## Overview

The `Student` class is designed to create and manage student objects with various attributes such as name, grade level, student ID, and email address. It demonstrates key object-oriented programming concepts including class methods, static methods, instance methods, and class variables.

## Features

- Create student objects with personal information
- Automatically generate university email addresses
- Format student IDs with university prefix
- Create student objects from full names
- Track all student instances
- Update student grade levels
- Display student information

## Class Structure

### Class Variables
- `school_name`: University name (Weber State University)
- `all_students`: List tracking all student instances

### Methods

#### Constructor
- `__init__(first_name, last_name, grade, student_id=None)`: Initializes a student with basic information

#### Class Methods
- `from_full_name(full_name, grade, student_id)`: Alternative constructor that creates a student from a full name
- `change_grade(new_grade_level)`: Updates a student's grade level
- `get_all_students()`: Returns list of all student instances

#### Static Methods
- `format_student_id(student_id)`: Formats student IDs with "WSU-" prefix

#### Instance Methods
- `print_student_data()`: Prints formatted student information
- `__str__()`: Returns string representation of student object

## Usage Examples

### Creating Student Objects

```python
# Creating student objects directly
jane = Student("Jane", "Doe", "Senior", 1233)
john = Student("John", "Doe", "Freshman", 1234)

# Creating a student from full name
waldo = Student.from_full_name("Waldo Wildcat", "Sophomore", 4567)
```

### Displaying Student Information

```python
# Display information for a single student
jane.print_student_data()

# Display all students using string representation
for student in Student.all_students:
    print(student)
```

### Updating Student Information

```python
# Change a student's grade level
jane.change_grade("Senior")
```

## Notes

- Student email addresses are automatically generated in the format: `firstnamelastname@mail.weber.edu`
- Student IDs are automatically formatted with "WSU-" prefix if provided
- If no student ID is provided, "No ID assigned" is used as a placeholder