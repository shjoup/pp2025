import math
import numpy




class Course:
    def __init__(self, courseid, coursename):
        self.__courseid = courseid
        self.__coursename = coursename

    def get_courseid(self):
        return self.__courseid
    def get_coursename(self):
        return self.__coursename

class Student:
    def __init__(self, studentid, studentname, dob):
        self.__studentid = studentid
        self.__studentname = studentname
        self.__dob = dob
        self.__marks = {}
        self.__avgmarks = {}

    def get_studentid(self):
        return self.__studentid
    def get_studentname(self):
        return self.__studentname
    def get_dob(self):
        return self.__dob
    def get_marks(self):
        return self.__marks
    def get_avgmarks(self):
        return numpy.mean(list(self.__marks.values()))

    def addmark(self, course, mark):
        self.__marks[course.get_coursename()] = mark


    def modmark(self, newcoursename, newmark):
        if newcoursename in self.__marks:
            self.__marks[newcoursename] = newmark
        else:
            print("Course not found")




nostudent = int(input("Enter number of students: "))
students = []

for _ in range(nostudent):
    studentid = int(input("Enter student id: "))
    studentname = input("Enter student name: ")
    studentdob = input("Enter student dob: ")

    studentinfo = Student(studentid, studentname, studentdob)

    nocourse = int(input("Enter number of courses: "))

    for _ in range(nocourse):
        courseid = input("Enter course id: ")
        coursename = input("Enter course name: ")
        mark = math.floor(float(input("Enter mark: ")))

        courseinfo = Course(courseid, coursename)
        studentinfo.addmark(courseinfo, mark)

    students.append(studentinfo)

for x in range(nostudent):
    print("========================================")
    print("Student name: ",students[x].get_studentname())
    print("Student id: ",students[x].get_studentid())
    print("Student dob: ",students[x].get_dob())
    print(students[x].get_marks())
    print("Gpa: ", students[x].get_avgmarks())
    print("========================================")

yn = input("Do you want to modify mark? y/n: ")
if yn.lower() == "y":

    key = input("Enter course to modify: ")
    key2 = math.floor(float(input("Enter mark: ")))

    for x in range(nostudent):
        students[x].modmark(key, key2)
        print("========================================")
        print("Student name: ",students[x].get_studentname())
        print("Student id: ",students[x].get_studentid())
        print("Student dob: ",students[x].get_dob())
        print(students[x].get_marks())
        print("Gpa: ", students[x].get_avgmarks())
        print("========================================")

elif yn.lower() == "n":
    print("Exiting")
