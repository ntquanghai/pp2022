import math
import numpy as np
import curses
from curses import wrapper


studentList = []

coursesList = [
    {
        "name": "LA",
        "credits": 3,
        "id": 0
    },
    {
        "name": "CN",
        "credits": 3,
        "id": 1
    },
    {
        "name": "PS",
        "credits": 3,
        "id": 2
    },
    {
        "name": "SE",
        "credits": 4,
        "id": 3
    },
    {
        "name": "Python",
        "credits": 5,
        "id": 4
    },
]


class Student:
    def __init__(self,stdscr):
        stdscr.addstr("Enter student's name: ")
        self.name = stdscr.getstr()
        # self.name = input("Enter student's name: ")

        stdscr.addstr("Enter student's ID: ")
        self.id_constant = stdscr.getstr()

        # self.id_constant = input("Enter student's ID: ")

        self.dob = self.inputStudentDOB(stdscr)
        self.courses = self.inputCourseEnrollment(stdscr)
    
    def getName(self):
        return self.name
    def getId(self):
        return self.id_constant
    def getDob(self):
        return self.dob
    def getCourses(self):
        return self.courses

    def inputStudentDOB(self,stdscr): 
        dayFlag = True
        while(dayFlag): 
            # dayInput = int(input("Enter the student's day of birth: "))
            stdscr.addstr("Enter the student's day of birth: ")
            dayInput = stdscr.getstr().decode()
            if(isinstance(int(dayInput), int)):
                if(int(dayInput)<32 and int(dayInput)>0):
                    dayFlag = False
                else:
                    stdscr.addstr("Entred day invalid. Please try again.")
            else:
                stdscr.addstr("Entred day invalid. Please try again.")
        monthFlag = True
        while(monthFlag):
            # monthInput = int(input("Enter the student's month of birth: "))
            stdscr.addstr("Enter the student's month of birth: ")
            monthInput = stdscr.getstr().decode()
            if(isinstance(int(monthInput), int)):
                if(int(monthInput) == 2 and int(dayInput)>29):
                    print("Entered month invalid. Please try again")
                    stdscr.addstr("Entered month invalid. Please try again")
                elif(int(monthInput)<13 and int(monthInput)>0):
                    monthFlag = False
                else:
                    print("Entered month invalid. Please try again")
                    stdscr.addstr("Entered month invalid. Please try again")
        # yearInput = int(input("Enter student's year of birth: "))
        stdscr.addstr("Enter student's year of birth: ")
        yearInput = int(stdscr.getstr().decode())

        returnedValue = str(dayInput)+"/"+str(monthInput)+"/"+str(yearInput)
        return returnedValue

    def showGrade(self,stdscr):
        # studentName = input("Enter name of the student: ")
        studentName = Utils.cursesInput(stdscr,"Enter the name of the student: ")

        # studentId = input("Enter ID of the student: ")
        studentId = Utils.cursesInput(stdscr, "Enter ID of the student: ")
        for i in range(0, len(studentList)):
            if(studentName == studentList[i]["name"] and studentId == studentList[i]["ID_CONSTANT"]):
                chosenCourse = input("Choose which course you want to see the grade of: ")
                print("Course: " + chosenCourse + " - Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"courseName",chosenCourse)]["grade"]))
                stdscr.addstr("Course: " + chosenCourse + " - Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"courseName",chosenCourse)]["grade"]))
            else:
                print("The student does not exist")
                stdscr.addstr("The student does not exist")
        
    def inputCourseEnrollment(self,stdscr):
        tempList = []
        returnedList = []
        index = 0

        # numOfCourses = int(input("Enter student's"+ " number of enrolled courses: "))
        numOfCourses = (Utils.cursesInput(stdscr,"Enter the student's number of enrolled courses"))

        inputFlag = True
        while(inputFlag):
            if(numOfCourses==0 or int(numOfCourses)>len(coursesList)):
                print("Invalid input. Please try again")
                stdscr.addstr("Invalid input. Please try again")
            else:
                inputFlag = False
        courses = Course.listCourse(coursesList)
        print("\n")
        while index < int(numOfCourses):
            # inputCourse = input("Enter student's course no." + str(index+1) +": ")
            inputCourse = Utils.cursesInput("Enter student's course no." + str(index+1) + ": ")

            if (inputCourse in tempList):
                # print("Course " + inputCourse + " has already been added. Please try again.")
                stdscr.addstr("Course " + inputCourse + " has already been added. Please try again.")
            elif (inputCourse in courses):
                addedCourse = {
                    "grade": "",
                    "courseName": inputCourse,
                }
                tempList.append(inputCourse)
                returnedList.append(addedCourse)
                index = index + 1
                print("Course "+inputCourse + " has been added")
                stdscr.addstr("Course" + inputCourse + " has been added")
            else:
                print("The entered course does not exist. Please try again.")
                stdscr.addstr("The entered course does not exist. Please try again.")

        return returnedList

        
class Course:
    def __init__(self, stdscr) -> None:
        # self.courseName = input("Enter course name: ")
        self.courseName = Utils.cursesInput(stdscr, "Enter course name: ")
        # self.courseId = input("Enter course ID: ")
        self.courseId = Utils.cursesInput(stdscr, "Enter course ID: ")
        # self.courseCredits = input("Enter course credits: ")
        self.courseCredits = Utils.cursesInput(stdscr, "Enter course credits: ")

    def listCourse(stdscr): 
        listOfCourse = []
        for i in range(0, len(coursesList)):
            listOfCourse.append(coursesList[i]["name"])

        # print("Here are the available courses:")
        stdscr.addstr("Here are the available courses")
        for i in range(0, len(coursesList)):
            # print(coursesList[i]["name"], end=" ")
            stdscr.addstr(coursesList[i]["name"]+ ", ")
        # print("\n")
        return listOfCourse

class Class:
    def __init__(self) -> None:
        self.studentList = []
        self.courseList = coursesList

    def inputStudentInfo(self, stdscr):
        # studentsNum = int(input("Enter the number of students: "))
        studentsNum = Utils.cursesInput(stdscr, "Enter the number of students:" )
        for i in range(0, int(studentsNum)):
            tempDict = {
                "name": "",
                "ID_CONSTANT": "",
                "dob":"",
                "courses": "",
                "GPA": 0,
            }
            tempStudent = Student(stdscr)

            tempDict["name"] = tempStudent.getName()
            tempDict["ID_CONSTANT"] = tempStudent.getId()
            tempDict["courses"] = tempStudent.getCourses()
            tempDict["dob"] = tempStudent.getDob()
            studentList.append(tempDict)
        
        return tempDict

    def inputCourseInfo(self, stdscr):
        # coursesNum = int(input("Enter the number of added courses: "))
        coursesNum = Utils.cursesInput(stdscr, "Enter the number of added courses:")
        for i in range(0, int(coursesNum)):
            tempDict = {
                "name":"",
                "id":"",
                "credits": "",
            }
            tempCourse = Course()

            tempDict["name"] = tempCourse.courseName
            tempDict["id"] = tempCourse.courseId
            tempDict["credits"] = tempCourse.courseCredits
            coursesList.append(tempDict)
        


    def listStudents(self, stdscr): 
        def listStudentCourse(studentCourseList):
            returnedCourseList = []
            for i in range(0, len(studentCourseList)):
                returnedCourseList.append(studentCourseList[i]["courseName"])
            return returnedCourseList
        
        for i in range(0,len(studentList)):
            stdscr.addstr("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))
            print("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))

    def modifyGrades(self, stdscr):
        checkList = []
        courses = Course.listCourse(coursesList)        
        if(not studentList):
            print("Student list is incomplete.")
            stdscr.addstr("Student list is incomplete.")
        else:
            # studentName = input("\nEnter student's name to modify grades: ")
            studentName = Utils.cursesInput(stdscr, "Enter student's name to modify gradeS: ")

            # studentID = input("Enter student's ID to modify grades: ")
            studentID = Utils.cursesInput(stdscr, "Enter student's ID to modify grades: ")
            if(Utils.find(studentList,"ID_CONSTANT",studentID)!=-1):            
                currentStudent = studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]
                print("Student: " + currentStudent["name"], "- ID: "+ currentStudent["ID_CONSTANT"] + "is enrolled in: ", end=" ")
                for i in range(0,len(currentStudent["courses"])):
                    print(currentStudent["courses"][i]["courseName"], end=" ")
                    checkList.append(currentStudent["courses"][i]["courseName"])
                courseInput = input("\nEnter student's course to modify grades: ")
                if(courseInput in checkList):
                    studentGrade = self.roundDownGrades(input("Enter the modified grade: "))
                    while((not isinstance(studentGrade,int)) or (not isinstance(studentGrade,float)) or isinstance>20 or isinstance<0):
                        print("Invalid input. Please try again")
                    (studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"][Utils.find(studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 
                else:
                    print("The course does not exist")
            else:
                print("The student does not exist.")   

    def roundDownGrades(self,input):
        return math.floor(input)

    def averageGrades(self, stdscr):
        # studentName = input("\nEnter student's name to see their average grades: ")
        studentName = Utils.cursesInput(stdscr, "Enter student's name to see their average grades: ")

        # studentID = input("Enter student's ID to see their average grades: ")
        studentID = Utils.cursesInput(stdscr, "Enter student's ID to see their average grades: ")
        gradeArray = np.array([])
        studentIndex = Utils.find(studentList,"ID_CONSTANT",studentID)
        if(studentIndex!=-1): 
            for i in range(0,len(studentList[studentIndex])):
                if((not isinstance(studentList[studentIndex]["courses"][i]["grade"],float)) or (not isinstance(studentList[studentIndex]["courses"][i]["grade"],int))):
                    gradeArray = np.append(0)
                else:
                    gradeArray = np.append(gradeArray, float(studentList[studentIndex]["courses"][i]["grade"]))
            averageGrade = np.average(gradeArray)
            (studentList[studentIndex]).update({"GPA":averageGrade})
            print(studentName+" - " + "ID: " +studentID + " - GPA: "+averageGrade)
            stdscr.addstr(studentName+" - " + "ID: " +studentID + " - GPA: "+averageGrade)
        else:
            print("The student does not exist")
            stdscr.addstr("The student does not exist")

    def sortStudentList(self):
        sortedStudentList = sorted(studentList.copy(), key= lambda d: d['GPA']) 
        return sortedStudentList
    

class Utils:
    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1
    
    def cursesInput(stdscr,string):
        curses.echo()
        stdscr.addstr(string)
        input = stdscr.getstr()

        return input.decode()

    

def main(stdscr): 
    stdscr.clear()
    stdscr.refresh()
    curses.echo()

    classroom = Class()

    while(True):
        print("#1. Enter students information (Name, ID, Date of birth, Enrolled courses)")
        stdscr.addstr("#1. Enter students information (Name, ID, Date of birth, Enrolled courses)")
        print("#2. Show students' grades")
        stdscr.addstr("#2. Show students' grades")
        print("#3. List all available students")
        stdscr.addstr("#3. List all available students")
        print("#4. List all available courses")
        stdscr.addstr("#4. List all available courses")
        print("#5. Add a course")
        stdscr.addstr("#5. Add a course")
        print("#6. Modify students' grades")
        stdscr.addstr("#6. Modify students' grades")
        print("#0. Exit the program")
        stdscr.addstr("#0. Exit the program")

        # option = int(input("Enter the option: "))
        option = Utils.cursesInput(stdscr, "Enter the option: ")

        if int(option) ==1:
            classroom.inputStudentInfo(stdscr)
        elif int(option) ==2:
            Student.showGrade(stdscr)
        elif int(option) ==3:
            classroom.listStudents(stdscr)
        elif int(option) ==4:
            Course.listCourse(stdscr)
        elif int(option) ==5:
            classroom.inputCourseInfo(stdscr)
        elif int(option) ==6:
            classroom.modifyGrades(stdscr)
        elif int(option) ==0:
            print("Session ended.")
            break

wrapper(main)


