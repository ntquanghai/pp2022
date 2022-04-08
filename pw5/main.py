import domains
import cursesInput
import output
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

def main(stdscr): 
    stdscr.clear()
    stdscr.refresh()
    curses.echo()

    while(True):
        # print("#1. Enter students information (Name, ID, Date of birth, Enrolled courses)")
        stdscr.addstr("#1. Enter students information (Name, ID, Date of birth, Enrolled courses) ")
        # print("#2. Show students' grades")
        stdscr.addstr("#2. Show students' grades ")
        # print("#3. List all available students")
        stdscr.addstr("#3. List all available students ")
        # print("#4. List all available courses")
        stdscr.addstr("#4. List all available courses ")
        # print("#5. Add a course")
        stdscr.addstr("#5. Add a course ")
        # print("#6. Modify students' grades ")
        stdscr.addstr("#6. Modify students' grades ")
        # print("#0. Exit the program")
        stdscr.addstr("#0. Exit the program ")

        # option = int(input("Enter the option: "))
        option = domains.Utils.cursesInput(stdscr, "Enter the option: ")

        if int(option) ==1:
            domains.Student.inputStudentInfo(stdscr, studentList)
        elif int(option) ==2:
            domains.Student.showGrade(stdscr, studentList)
        elif int(option) ==3:
            domains.Class.listStudents(stdscr, studentList)
        elif int(option) ==4:
            domains.Course.listCourse(stdscr, coursesList)
        elif int(option) ==5:
            domains.Course.inputCourseInfo(stdscr, coursesList)
        elif int(option) ==6:
            domains.Class.modifyGrades(stdscr, studentList)
        elif int(option) ==0:
            print("Session ended.")
            break

wrapper(main)