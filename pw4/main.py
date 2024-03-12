
import math
from input import get_course_input, get_student_input, input_mark
from output import list_course, display_student


def main():
    course_count = int(input("Enter number of courses: "))
    course_library = get_course_input(course_count)

    student_count = int(input("Enter number of student: "))
    student_library = get_student_input(student_count)

    list_course(course_library)

    input_mark(student_library, course_library) # input mark
    display_student(student_library)
    for student in student_library:
        weighted_sum = student.calculate_weighted_sum_credits_and_mark(course_library)
        print(f"The weighted sum for {student.get_name()} is {weighted_sum}")
    gpa_list = {}
    for student in student_library:  # calculate gpa of all student input
        gpa_list[student.get_name()] = student.calculate_average_gpa()

    sorted_gpa_list = sorted(gpa_list.items(), key=lambda x: x[1], reverse=True)
    print("\nGPA after sorting:")
    for student, gpa in sorted_gpa_list:
        print(f"{student}: {gpa}")


if __name__ == "__main__":
    main()


