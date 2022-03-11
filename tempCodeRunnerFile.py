
studentList = [
]

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
    {
        "name": "Hello",
        'courses': [{'grade': '', 'courseName': 'LA'}, {'grade': '', 'courseName': 'CN'}]
    }
]

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

haha = [{'name': 'Harry', 'ID_CONSTANT': '1', 'courses': [{'grade': '', 'courseName': 'Python'}, {'grade': '', 'courseName': 'LA'}]}]


def inputStudentNum():
    num = int(input("Enter the number of students: "))
    return num


def chooseCourse(courseList, studentList):
    listOfCourse = []
    flag = True
    studentCourseList = []
    for i in range(0, len(courseList)):
        listOfCourse.append(courseList[i]["name"])

    print("Here are the available courses: \n")
    for i in range(0, len(courseList)):
        print(courseList[i]["name"], end=" ")
    print("\n")
    courseInput = input("Enter the course name: ")
    print("hello " + str(studentList))
    while flag:
        if(courseInput in listOfCourse):
            for i in range(0, len(studentList)):
                for t in range (0, len((studentList[i]["courses"]))):
                    if(studentList[i]["courses"][t]["courseName"] == courseInput):
                        studentCourseList.append(studentList[i])
            flag = False
        else:
            print("The entered course does not exist. Please try again.")
    
    if(not studentList):
        print("Student list is incomplete.")
    else:
        studentName = input("Enter student's name to modify grades: ")
        studentID = input("Enter student's ID to modify gradeS: ")
        for i in range(0, len(studentCourseList)):
            if((studentName == studentCourseList[i]["name"]) and [studentID == studentCourseList[i]["ID_CONSTANT"]]):
                studentGrade = input("Enter student "+ studentName + ", ID: "+ studentID + " new grade: ")
                (studentList[find(studentList,"ID_CONSTANT",studentID)]["courses"][find(studentList[find(studentList,"ID_CONSTANT",studentID)]["courses"],"courseName",courseInput)]).update({"grade":studentGrade}) 
    print(studentList)
                


def inputCourseInfo(studentNo, courseList):
    listOfCourse = []
    tempList = []
    returnedList = []
    index = 0
    for i in range(0, len(courseList)):
        listOfCourse.append(courseList[i]["name"])

    numOfCourses = input("Enter student's no. " +
    str(studentNo) + " number of enrolled courses: ")

    print("==============================================================")
    print("Here are the available courses:")

    for i in range(0, len(courseList)):
        print(courseList[i]["name"], end=" ")
    print("\n")
    while index < int(numOfCourses):
        inputCourse = input("Enter course name no. " + str(index) +" for student no. " + str(studentNo) + ": ")
        if (inputCourse in tempList):
            print("Course " + inputCourse + " has already been added. Please try again.")
        elif (inputCourse in listOfCourse):
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

    print(returnedList)
    return returnedList


def inputStudentInfo(studentsNum, studentList):
    for i in range(0, studentsNum):
        tempDict = {
            "name": "",
            "ID_CONSTANT": "",
            "courses": "",
        }
        tempName = input("Enter the name for student no." + str(i) + ": ")
        tempId = input("Enter the ID for student no." + str(i) + ": ")
        courseList = inputCourseInfo(i, coursesList)

        tempDict["name"] = tempName
        tempDict["ID_CONSTANT"] = tempId
        tempDict["courses"] = courseList
        studentList.append(tempDict)

    print(studentList)
    return studentList


def initiateClass():
    numOfStudents = inputStudentNum()
    inputStudentInfo(numOfStudents, studentList)
    chooseCourse(coursesList,studentList)


initiateClass()
