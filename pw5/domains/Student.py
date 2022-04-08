import math
import numpy as np
import curses
from curses import wrapper
import Utils
import Course
import json

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

    def showGrade(self,stdscr, studentList):
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
        
    def inputCourseEnrollment(self,stdscr, coursesList):
        tempList = []
        returnedList = []
        index = 0

        # numOfCourses = int(input("Enter student's"+ " number of enrolled courses: "))
        numOfCourses = (Utils.cursesInput(stdscr,"Enter the student's number of enrolled courses: "))

        inputFlag = True
        while(inputFlag):
            if(numOfCourses==0 or int(numOfCourses)>len(coursesList)):
                print("Invalid input. Please try again")
                stdscr.addstr("Invalid input. Please try again")
            else:
                inputFlag = False
        courses = Course.listCourse(stdscr)
        print("\n")
        while index < int(numOfCourses):
            # inputCourse = input("Enter student's course no." + str(index+1) +": ")
            inputCourse = Utils.cursesInput(stdscr,"Enter student's course no." + str(index+1) + ": ")

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
    
    def inputStudentInfo(stdscr, studentList):
        # studentsNum = int(input("Enter the number of students: "))
        studentsNum = Utils.cursesInput(stdscr, "Enter the number of students: " )
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
            with open("../studentList.txt","w") as f:
                f.write(json.dumps(tempDict))
            studentList.append(tempDict)
        
        return tempDict