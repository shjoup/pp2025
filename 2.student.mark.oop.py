class Course:
    def __init__(self, courseid, coursename):
        self.courseid = courseid
        self.coursename = coursename

class Student:
    def __init__(self, studentid, studentname, dob):
        self.studentid = studentid
        self.studentname = studentname
        self.dob = dob
        self.marks = {}
        self.courses = {}

    def addmark(self, course, mark):
        self.marks[course.coursename] = mark
        self.courses[course.coursename] = course

    def modmark(self, newcoursename, newmark):
        if newcoursename in self.marks:
            self.marks[newcoursename] = newmark
        else:
            print("Course not found")

nostudent = int(input("Enter number of students "))
student = []

for _ in range(nostudent):
    studentid = int(input("Enter student id "))
    studentname = input("Enter student name ")
    studentdob = input("Enter student dob ")

    studentinfo = Student(studentid, studentname, studentdob)

    nocourse = int(input("Enter number of courses "))

    for _ in range(nocourse):
        courseid = int(input("Enter course id "))
        coursename = input("Enter course name ")
        mark = int(input("Enter mark "))

        courseinfo = Course(courseid, coursename)
        studentinfo.addmark(courseinfo, mark)

    student.append(studentinfo)

key = input("Enter course to modify ")
key2 = input("Enter mark ")

student[0].modmark(key, key2)

print("Student name: ",student[0].studentname)
print("Student id: ",student[0].studentid)
print("Student dob: ",student[0].dob)

print(student[0].marks)
