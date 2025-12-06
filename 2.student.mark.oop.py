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


    def addmark(self, course, mark):
        self.marks[course.coursename] = mark


    def modmark(self, newcoursename, newmark):
        if newcoursename in self.marks:
            self.marks[newcoursename] = newmark
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
        mark = int(input("Enter mark: "))

        courseinfo = Course(courseid, coursename)
        studentinfo.addmark(courseinfo, mark)

    students.append(studentinfo)

for x in range(nostudent):
    print("Student name: ",students[x].studentname)
    print("Student id: ",students[x].studentid)
    print("Student dob: ",students[x].dob)
    print(students[x].marks)


key = input("Enter course to modify: ")
key2 = int(input("Enter mark: "))

for x in range(nostudent):
    students[x].modmark(key, key2)

    print("Student name: ",students[x].studentname)
    print("Student id: ",students[x].studentid)
    print("Student dob: ",students[x].dob)
    print(students[x].marks)
