
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
