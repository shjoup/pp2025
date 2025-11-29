nostudent = input("Enter the number of student: ")
studentid = input("Enter the student id: ")
studentname = input("Enter student name: ")
studentdob = input("Enter student dob: ")
nocourse = input("Enter number of course: ")
courseid = input("Enter course id: ")
coursename = input("Enter course name: ")
mark = input("Enter mark: ")
studentmarkdict = {"Name": studentname, "Student id": studentid, "Student name": studentname, "Student DoB": studentdob, "Course id": courseid, coursename: coursename, "Mark": mark}

key = input("Enter course to modify: ")

if key in studentmarkdict:
    value = input(f"Enter the new mark for '{key}': ")
    studentmarkdict[mark] = value

    print(studentmarkdict)

else:
    print("Key not found")

