import math
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__course_mark = {}

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def input_mark(self, course, mark):
        self.__course_mark[course] = mark

    def display(self):
        print("Student: ", self.__name, "\nID: ", self.__id, "\nDOB: ", self.__dob)
        print(f"Mark for {self.__name} in: ")
        for course, mark in self.__course_mark.items():
            print(f"{course}: {mark}")

    def calculate_average_gpa(self):
        marks = list(self.__course_mark.values())
        gpa_array = np.array(marks)
        average_gpa = np.average(gpa_array)
        return average_gpa

    def calculate_weighted_sum_credits_and_mark(self, course_library):
        total_weighted_sum = 0
        for course in course_library:
            course_name = course.get_name()
            mark = self.__course_mark[course_name]
            weighted_sum = course.get_num_credits() * mark
            total_weighted_sum += weighted_sum

        return total_weighted_sum


class Course:
    def __init__(self, id, name, num_credits):
        self.__id = id
        self.__name = name
        self.__num_credits = num_credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_num_credits(self):
        return self.__num_credits

    def display(self):
        print("Course: ", self.__name, "\nID: ", self.__id)


def list_course():
    for i in range(course_count):
        course_library[i].display()


course_library = []
course_count = int(input("Enter number of course: "))
for i in range(course_count):  # input course
    course_name = input(f"Enter name for course {i + 1}: ")
    course_id = input(f"Enter id for course {i + 1}: ")
    course_credit = int(input(f"Enter credit for course {i + 1}:"))
    course_library.append(Course(course_id, course_name, course_credit))
list_course()

student_library = []
student_count = int(input("Enter number of student: "))
for i in range(student_count):
    student_name = input(f"Enter name of student {i + 1}: ")
    student_id = input(f"Enter id for student {i + 1}: ")
    student_dob = input(f"Enter date of birth (Y-M-D) for student {i + 1}:")
    student_library.append(Student(student_id, student_name, student_dob))

for student in student_library:
    for course in course_library:
        mark = float(input(f"Enter mark for {student.get_name()} in {course.get_name()}: "))
        student.input_mark(course.get_name(), math.floor(mark * 10) / 10)

for i in range(student_count):
    student_library[i].display()


for student in student_library:
    weighted_sum = student.calculate_weighted_sum_credits_and_mark(course_library)
    print(f"The weighted sum for {student.get_name()} is {weighted_sum}")

gpa_list = {}
for student in student_library:  # calculate gpa of all student input
    gpa_list[student.get_name()] = student.calculate_average_gpa()


# Print GPA before sorting
print("GPA before sorting:")
for student, gpa in gpa_list.items():
    print(f"{student}: {gpa}")

# Sort gpa_list
sorted_gpa_list = sorted(gpa_list.items(), key=lambda x: x[1], reverse=True)

# Print GPA after sorting
print("\nGPA after sorting:")
for student, gpa in sorted_gpa_list:
    print(f"{student}: {gpa}")