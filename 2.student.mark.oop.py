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

    def display(self, course_count):
        print("Student: ", self.__name, "\nID: ", self.__id, "\nDOB: ", self.__dob)
        print(f"Mark for {self.__name} in: ")
        #for i in range(course_count):
        #    print(f"{course_library[i].get_name()} : {self.__course_mark[course_library[i].get_name()]} ")
        for course, mark in self.__course_mark.items():
            print(f"{course}: {mark}")



class Course:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

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
    course_library.append(Course(course_id, course_name))
list_course()




student_library = []
student_count = int(input("Enter number of student: "))
for i in range(student_count):
    student_name = input(f"Enter name of student {i+1}: ")
    student_id = input(f"Enter id for student {i+1}: ")
    student_dob = input(f"Enter date of birth (Y-M-D) for student {i+1}:")
    student_library.append(Student(student_id,student_name,student_dob))


for student in student_library:
    for course in course_library:
        mark = input(f"Enter mark for {student.get_name()} in {course.get_name()}: ")
        student.input_mark(course.get_name(), mark)


for i in range(student_count):
    student_library[i].display(course_count)

# for i in range(student_count):
#     for j in range(course_count):
#         mark = input(f"Enter mark for student {student_library[i].get_name()} in {course_library[j].get_name()}: ")
#         student_library[i].input_mark(course_library[j].get_name(), mark)


