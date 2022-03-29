studentList = []

coursesList = [
    {
        "name": "LA",
        "id": 0
    },
    {
        "name": "CN",
        "id": 1
    },
    {
        "name": "PS",
        "id": 2
    },
    {
        "name": "SE",
        "id": 3
    },
    {
        "name": "Python",
        "id": 4
    },
]

class Student:
    def __init__(self):
        self.name = input("Enter student's name: ")
        self.id_constant = input("Enter student's ID: ")
        self.dob = self.inputStudentDOB()
        self.courses = self.inputCourseEnrollment()
    
    def getName(self):
        return self.name
    def getId(self):
        return self.id_constant
    def getDob(self):
        return self.dob
    def getCourses(self):
        return self.courses

    def inputStudentDOB(self): 
        dayFlag = True
        while(dayFlag): 
            dayInput = int(input("Enter the student's day of birth: "))
            if(isinstance(dayInput, int)):
                if(dayInput<32 and dayInput>0):
                    dayFlag = False
                else:
                    print("Entred day invalid. Please try again.")
            else:
                print("Entred day invalid. Please try again.")
        monthFlag = True
        while(monthFlag):
            monthInput = int(input("Enter the student's month of birth: "))
            if(isinstance(monthInput, int)):
                if(monthInput == 2 and dayInput>29):
                    print("Entered month invalid. Please try again")
                elif(monthInput<13 and monthInput>0):
                    monthFlag = False
                else:
                    print("Entered month invalid. Please try again")
        yearInput = int(input("Enter student's year of birth: "))

        returnedValue = str(dayInput)+"/"+str(monthInput)+"/"+str(yearInput)
        return returnedValue

    def showGrade(self):
        print("=== Show student's grades ===")
        studentName = input("Enter name of the student: ")
        studentId = input("Enter ID of the student: ")
        for i in range(0, len(studentList)):
            if(studentName == studentList[i]["name"] and studentId == studentList[i]["ID_CONSTANT"]):
                chosenCourse = input("Choose which course you want to see the grade of: ")
                print("Course: " + chosenCourse + " - Grade: " + str(studentList[i]["courses"][Utils.find(studentList[i]["courses"],"courseName",chosenCourse)]["grade"]))
                return
            else:
                print("The student does not exist")
        
    def inputCourseEnrollment(self):
        print("=== Student enrollment information ===")
        tempList = []
        returnedList = []
        index = 0

        numOfCourses = int(input("Enter student's"+ " number of enrolled courses: "))

        inputFlag = True
        while(inputFlag):
            if(numOfCourses==0 or int(numOfCourses)>len(coursesList)):
                print("Invalid input. Please try again")
            else:
                inputFlag = False
        courses = Course.listCourse(coursesList)
        print("\n")
        while index < int(numOfCourses):
            inputCourse = input("Enter student's course no." + str(index+1) +": ")
            if (inputCourse in tempList):
                print("Course " + inputCourse + " has already been added. Please try again.")
            elif (inputCourse in courses):
                addedCourse = {
                    "grade": "",
                    "courseName": inputCourse,
                }
                tempList.append(inputCourse)
                returnedList.append(addedCourse)
                index = index + 1
                print("Course "+inputCourse + " has been added")
            else:
                print("The entered course does not exist. Please try again.")

        return returnedList

        
class Course:
    def __init__(self) -> None:
        self.courseName = input("Enter course name: ")
        self.courseId = input("Enter course ID: ")

    def listCourse(): 
        print("=== Listing courses ===")
        listOfCourse = []
        for i in range(0, len(coursesList)):
            listOfCourse.append(coursesList[i]["name"])

        print("Here are the available courses:")
        for i in range(0, len(coursesList)):
            print(coursesList[i]["name"], end=" ")
        print("\n")
        return listOfCourse



class Class:
    def __init__(self) -> None:
        self.studentList = []
        self.courseList = coursesList

    def inputStudentInfo(self):
        studentsNum = int(input("Enter the number of students: "))
        for i in range(0, studentsNum):
            tempDict = {
                "name": "",
                "ID_CONSTANT": "",
                "dob":"",
                "courses": "",
            }
            tempStudent = Student()

            tempDict["name"] = tempStudent.getName()
            tempDict["ID_CONSTANT"] = tempStudent.getId()
            tempDict["courses"] = tempStudent.getCourses()
            tempDict["dob"] = tempStudent.getDob()
            studentList.append(tempDict)
        
        return tempDict

    def inputCourseInfo(self):
        print("=== Course input information ===")
        coursesNum = int(input("Enter the number of added courses: "))
        for i in range(0, coursesNum):
            tempDict = {
                "name":"",
                "id":"",
            }
            tempCourse = Course()

            tempDict["name"] = tempCourse.courseName
            tempDict["id"] = tempCourse.courseId
            coursesList.append(tempDict)
        


    def listStudents(self): 
        print("=== Listing students ===")
        def listStudentCourse(studentCourseList):
            returnedCourseList = []
            for i in range(0, len(studentCourseList)):
                returnedCourseList.append(studentCourseList[i]["courseName"])
            return returnedCourseList
        
        for i in range(0,len(studentList)):
            print("Student: "+ str(studentList[i]["name"]) + " ID: " + str(studentList[i]["ID_CONSTANT"]) + "- Enrolled in courses: " + str(listStudentCourse(studentList[i]["courses"])))

    def chooseCourse(self):
        print("=== Modify course grade ===")
        flag = True
        checkList = []
        courses = Course.listCourse(coursesList)        
        if(not studentList):
            print("Student list is incomplete.")
        else:
            studentName = input("\nEnter student's name to modify grades: ")
            studentID = input("Enter student's ID to modify grades: ")
            if(Utils.find(studentList,"ID_CONSTANT",studentID)!=-1):            
                currentStudent = studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]
                print("Student: " + currentStudent["name"], "- ID: "+ currentStudent["ID_CONSTANT"] + "is enrolled in: ", end=" ")
                for i in range(0,len(currentStudent["courses"])):
                    print(currentStudent["courses"][i]["courseName"], end=" ")
                    checkList.append(currentStudent["courses"][i]["courseName"])
                courseInput = input("\nEnter student's course to modify grades: ")
                if(courseInput in checkList):
                    studentGrade = input("Enter the modified grade: ")
                    (studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"][Utils.find(studentList[Utils.find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade})                 
                else:
                    print("The course does not exist")
            else:
                print("The student does not exist.")    

class Utils:
    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1

def main(): 
    classroom = Class()
    while(True):
        print("#1. Enter students information (Name, ID, Date of birth, Enrolled courses)")
        print("#2. Show students' grades")
        print("#3. List all available students")
        print("#4. List all available courses")
        print("#5. Add a course")
        print("#6. Modify students' grades")
        print("#0. Exit the program")

        option = int(input("Enter the option: "))
        if option ==1:
            classroom.inputStudentInfo()
        elif option ==2:
            Student.showGrade()
        elif option ==3:
            classroom.listStudents()
        elif option ==4:
            Course.listCourse()
        elif option ==5:
            classroom.inputCourseInfo()
        elif option ==6:
            classroom.chooseCourse()
        elif option ==0:
            print("Session ended.")
            break

main()


