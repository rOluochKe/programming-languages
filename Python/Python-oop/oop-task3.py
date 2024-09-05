"""
Title: Online Course Enrollment and Grading System

Description:
This code represents a system for enrolling students in online courses and calculating their average grades. Let's break it down in simpler terms.

Hint -> Use the code from the previous video
###

Imagine you have an online platform where you can create courses and teach them. The code helps you manage those courses and keep track of students and their grades.

Here's how it works:

Creating a Course:
When you create a new course, you give it a name and the name of the instructor. The system keeps a list of students who enroll in the course.

#1 - Enrolling Students -> enroll_student(student):
You can enroll students in a course. Each student has a name and a few grades. When you enroll a student, the system adds their name to the list of enrolled students for that course. It tells you that the student has successfully enrolled. It takes a Student object as input, which includes the student's name and a list of grades

#2 - Checking Course Details -> get_course_details():
You can ask the system to show you details about a course. This includes the course name, the instructor's name, and the names of all the students who have enrolled.

#3 - Completing a Course -> complete_course(student_name):
When a student finishes a course, you can mark them as completed. The system removes their name from the list of enrolled students and tells you that the student has successfully completed the course. But if you try to mark someone as completed who is not enrolled in the course, the system tells you that the student is not in the course.

#4 - Calculating Average Grade -> calculate_average_grade():
You can also ask the system to calculate the average grade for all students in a course. It adds up the grades of all the students and divides it by the total number of grades. This gives you an average grade, which represents how well the students performed on average.

#####

Outside your class, you can try out the system. You can enter the course name, the instructor's name, and the number of students you want to enroll. For each student, you enter their name and three grades.

Then, the system enrolls the students, calculates the average grade for all students in the course, and shows you the course details.

This code helps make it easier to manage online courses and keep track of students' progress. It lets you enroll students, see course information, mark students as completed, and calculate average grades.
"""


class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_students(self, student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course} course.")

    def course_details(self):
        print(f"Course: {self.course}")
        print(f"Instructor Name: {self.instructor}")
        print("Enrolled Students:")
        for student in self.students:
            print(student.name)

    def completed_course(self, name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
                print(f"{name} has completed the course!")
        print(f"{name} is not enrolled in this course")

    def avg_grade(self, grades):
        total = sum(student.grades)
        average = total / len(student.grades)
        print(f"The average grade is: {round(average,1)}")


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


course_input = input("Enter a course: ").lower()
name = input("Enter a Instructor: ").lower()
course = OnlineCourse(course_input, name)

num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    student_name = input("Enter a student name:  ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter a grade:  "))
        grades.append(grade)
    student = Student(student_name, grades)
    course.enroll_students(student)
    course.avg_grade(student)
course.course_details()
