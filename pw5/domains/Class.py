import Course
import Utils
import math
import numpy as np
import json


class Class:
    def __init__(self, studentList, coursesList):
        self.studentList = []
        self.courseList = coursesList
        
    def listStudents(stdscr, studentList): 
        def listStudentCourse(studentCourseList):
            returnedCourseList = []
            for i in range(0, len(studentCourseList)):
                returnedCourseList.append(studentCourseList[i]["courseName"])
            return returnedCourseList
        
        for i in range(0,len(studentList)):
            stdscr.addstr("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))
            print("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))

    def modifyGrades(stdscr, studentList):
        checkList = []
        courses = Course.listCourse(stdscr)        
        if(not studentList):
            print("Student list is incomplete.")
            stdscr.addstr("Student list is incomplete.")
        else:
            # studentName = input("\nEnter student's name to modify grades: ")
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
                    studentGrade = Class.roundDownGrades(input("Enter the modified grade: "))
                    while((not isinstance(studentGrade,int)) or (not isinstance(studentGrade,float)) or isinstance>20 or isinstance<0):
                        print("Invalid input. Please try again")
                    (studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"][Utils.find(studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 
                else:
                    print("The course does not exist")
            else:
                print("The student does not exist.")   

    def roundDownGrades(self,input):
        return math.floor(input)

    def averageGrades(stdscr, studentList):
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

    def sortStudentList(self, studentList):
        sortedStudentList = sorted(studentList.copy(), key= lambda d: d['GPA']) 
        return sortedStudentList