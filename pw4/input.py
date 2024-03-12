from domains.course import Course
from domains.student import Student
import math


def get_course_input(course_count):
    course_library = []

    for i in range(course_count):
        course_name = input(f"Enter name for course {i + 1}: ")
        course_id = input(f"Enter id for course {i + 1}: ")
        course_credit = int(input(f"Enter credit for course {i + 1}:"))
        course_library.append(Course(course_id, course_name, course_credit))
    return course_library


def get_student_input(student_count):
    student_library = []

    for i in range(student_count):
        student_name = input(f"Enter name of student {i + 1}: ")
        student_id = input(f"Enter id for student {i + 1}: ")
        student_dob = input(f"Enter date of birth (Y-M-D) for student {i + 1}:")
        student_library.append(Student(student_id, student_name, student_dob))
    return student_library


def input_mark(student_library, course_library):
    for student in student_library:
        for course in course_library:
            mark = float(input(f"Enter mark for {student.get_name()} in {course.get_name()}: "))
            student.input_mark(course.get_name(), math.floor(mark * 10) / 10)
