import Utils
import cursesInput

class Course:
    def __init__(self, stdscr) -> None:
        # self.courseName = input("Enter course name: ")
        self.courseName = Utils.cursesInput(stdscr, "Enter course name: ")
        # self.courseId = input("Enter course ID: ")
        self.courseId = Utils.cursesInput(stdscr, "Enter course ID: ")
        # self.courseCredits = input("Enter course credits: ")
        self.courseCredits = Utils.cursesInput(stdscr, "Enter course credits: ")

    def listCourse(stdscr, coursesList): 
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

    def inputCourseInfo(stdscr, coursesList):
        # coursesNum = int(input("Enter the number of added courses: "))
        coursesNum = Utils.cursesInput(stdscr, "Enter the number of added courses: ")
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