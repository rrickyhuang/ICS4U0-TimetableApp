import csv
import sys
from tkinter import *


class Course:
    """
    A course object that holds the course information, including: Course code, course name, instructor, the semester
    and period the course is running, the class size, the grade level of the course, and the prerequisites for the
    course.

    Attributes
    ----------
    code : str
        The course code.
    name : str
        The name of the course.
    instructor : str
        The instructor of the course.
    semester : int
        The semester that the course will run.
    period : int
        The period that the course will run.
    grade : int
        The intended grade level of the course.
    prerequisites : list
        The prerequisite courses of this course.

    Methods
    --------
    printCourse() -> None
        Prints the course information to the console.

    """

    def __init__(self, code, name, instructor, semester, period, size, grade, prerequisites):
        self.code = code
        self.name = name
        self.instructor = instructor
        self.semester = semester
        self.period = period
        self.size = size
        self.grade = grade
        self.prerequisites = prerequisites

    def printCourse(self) -> None:
        print(self.code)
        print(self.name)
        print(self.instructor)
        print(self.semester)
        print(self.period)
        print(self.size)
        print(self.grade)
        print(self.prerequisites)
        return


class Student:

    def __init__(self, number, name, grade):
        self.number = number
        self.name = name
        self.grade = grade

    def printStudentInfo(self) -> None:
        print(self.number)
        print(self.name)
        print(self.grade)
        return


class Timetable:

    def __init__(self, number, semesterOnePeriodOne, semesterOnePeriodTwo, semesterOnePeriodThree,
                 semesterOnePeriodFour, semesterTwoPeriodOne, semesterTwoPeriodTwo, semesterTwoPeriodThree,
                 semesterTwoPeriodFour):
        self.number = number
        self.semesterOnePeriodOne = semesterOnePeriodOne
        self.semesterOnePeriodTwo = semesterOnePeriodTwo
        self.semesterOnePeriodThree = semesterOnePeriodThree
        self.semesterOnePeriodFour = semesterOnePeriodFour
        self.semesterTwoPeriodOne = semesterTwoPeriodOne
        self.semesterTwoPeriodTwo = semesterTwoPeriodTwo
        self.semesterTwoPeriodThree = semesterTwoPeriodThree
        self.semesterTwoPeriodFour = semesterTwoPeriodFour

    def printTimetable(self) -> None:
        print(self.student)
        print(self.grade)
        print(self.number)
        print(self.periodOne)
        print(self.periodTwo)
        print(self.periodThree)
        print(self.periodFour)
        return


class ChosenCourses:

    def __init__(self, number, course1, course2, course3, course4, course5, course6, course7, course8, alt1, alt2):
        self.number = number
        self.course1 = course1
        self.course2 = course2
        self.course3 = course3
        self.course4 = course4
        self.course5 = course5
        self.course6 = course6
        self.course7 = course7
        self.course8 = course8
        self.alt1 = alt1
        self.alt2 = alt2

    def printChosenCourses(self) -> None:
        print(self.number)
        print(self.course1)
        print(self.course2)
        print(self.course3)
        print(self.course4)
        print(self.course5)
        print(self.course6)
        print(self.course7)
        print(self.course8)
        print(self.alt1)
        print(self.alt2)
        return


def mainMenu():
    mainMenuWindow = Tk()

    mainMenuWindow.title("Timetable App - Main Menu")

    mainMenuChoice = IntVar(value=1)

    counsellorChoice = Radiobutton(mainMenuWindow, text="I am a counsellor", variable=mainMenuChoice, value=1,
                                   tristatevalue=0)
    counsellorChoice.pack()
    studentChoice = Radiobutton(mainMenuWindow, text="I am a student", variable=mainMenuChoice, value=2,
                                tristatevalue=0)
    studentChoice.pack()

    confirmButton = Button(mainMenuWindow, text="Confirm", command=mainMenuWindow.quit)
    confirmButton.pack()

    mainMenuWindow.mainloop()
    mainMenuWindow.destroy()

    return mainMenuChoice.get()

    '''
    while True:
        print('Are you a guidance counsellor or student?')
        print('1 : Counsellor')
        print('2 : Student')
        print('3 : Exit')
        mainMenuChoice = int(input())
        if mainMenuChoice >= 1 and mainMenuChoice <= 3:
            return mainMenuChoice
        continue
'''


def counsellorMenu():
    counsellorMenu = Tk()

    counsellorMenu.title("Timetable App - Counsellor Menu")

    counsellorMenuChoice = IntVar(value=9)

    viewCourseChoice = Radiobutton(counsellorMenu, text="View courses", variable=counsellorMenuChoice, value=1,
                                   tristatevalue=0)
    viewCourseChoice.grid(column=0, row=0)

    addCourseChoice = Radiobutton(counsellorMenu, text="Add new course", variable=counsellorMenuChoice, value=2,
                                  tristatevalue=0)
    addCourseChoice.grid(column=0, row=1)

    editCourseChoice = Radiobutton(counsellorMenu, text="Edit a course", variable=counsellorMenuChoice, value=3,
                                   tristatevalue=0)
    editCourseChoice.grid(column=0, row=2)

    deleteCourseChoice = Radiobutton(counsellorMenu, text="Delete a course", variable=counsellorMenuChoice, value=4,
                                     tristatevalue=0)
    deleteCourseChoice.grid(column=0, row=3)

    viewStudentsChoice = Radiobutton(counsellorMenu, text="View all students", variable=counsellorMenuChoice, value=5,
                                     tristatevalue=0)
    viewStudentsChoice.grid(column=1, row=0)

    addStudentChoice = Radiobutton(counsellorMenu, text="Add new student", variable=counsellorMenuChoice, value=6,
                                   tristatevalue=0)
    addStudentChoice.grid(column=1, row=1)

    editStudentChoice = Radiobutton(counsellorMenu, text="Edit student info", variable=counsellorMenuChoice, value=7,
                                    tristatevalue=0)
    editStudentChoice.grid(column=1, row=2)

    deleteStudentChoice = Radiobutton(counsellorMenu, text="Remove a student", variable=counsellorMenuChoice, value=8,
                                      tristatevalue=0)
    deleteStudentChoice.grid(column=1, row=3)

    returnToMainMenuChoice = Radiobutton(counsellorMenu, text="Return to Main Menu", variable=counsellorMenuChoice,
                                         value=9,
                                         tristatevalue=0)
    returnToMainMenuChoice.grid(column=1, row=100)

    confirmButton = Button(counsellorMenu, text="Confirm", command=counsellorMenu.quit)
    confirmButton.grid(column=0, row=100)

    counsellorMenu.mainloop()
    counsellorMenu.destroy()

    return counsellorMenuChoice.get()
    '''
    while True:
        print('What do you want to do?')
        print('1 : View courses')
        print('2 : Add new course')
        print('3 : Edit course')
        print('4 : Delete course')
        print('5 : View students')
        print('6 : Add new student')
        print('7 : Edit student info')
        print('8 : Delete student')
        print('9 : Return to main menu')
        counsellorMenuChoice = int(input())
        if counsellorMenuChoice >= 1 and counsellorMenuChoice <= 9:
            return counsellorMenuChoice
        continue
'''


def studentMenu():
    while True:
        print('What do you want to do?')
        print('1 : Choose courses')
        print('2 : View chosen courses')
        print('3 : View timetable')
        print('4 : Change courses')
        print('5 : Return to main menu')
        studentMenuChoice = int(input())
        if studentMenuChoice >= 1 and studentMenuChoice <= 5:
            return studentMenuChoice
        continue


def printAllCourses():
    with open("courses.txt", "r") as courses:
        rd = csv.reader(courses, delimiter=',')

        for line in rd:
            print('Course Code: ', line[0], 'Course Name: ', line[1], 'Course Instructor: ', line[2], 'Semester ',
                  line[3], ', Period ', line[4], 'Class Size: ', line[5], 'Grade ', line[6], 'Prerequisites: ',
                  line[7])
    return


def createCourse():
    code = input("input course code")
    name = input("input course name")
    instructor = input("input course instructor")
    semester = input("what semester will the course run?")
    period = input("what period will the course run?")
    size = input("what is the max size of the class")
    grade = input('what grade is the course for?')
    prerequisites = input('input prerequisite course code')

    newCourse = Course(code, name, instructor, semester, period, size, grade, prerequisites)

    print('New course created:')
    newCourse.printCourse()
    with open("courses.txt", "at", newline='') as courses:
        wr = csv.writer(courses, delimiter=',', quotechar='"')
        wr.writerow([code, name, instructor, semester, period, size, grade, prerequisites])
    return


def deleteCourse():
    code = input('input the code of the course you want to delete.')

    with open("courses.txt", "r") as courses:
        lines = courses.readlines()
    with open("courses.txt", "w") as courses:
        for line in lines:
            if not line.startswith(code):
                courses.write(line)
    return


def printAllStudents():
    with open("students.txt", "r") as students:
        rd = csv.reader(students, delimiter=',')

        for line in rd:
            print('Student Number: ', line[0], 'Student Name: ', line[1], 'Grade: ', line[2])
    return


def addStudent():
    number = input("Input student number")
    name = input("Input student's name")
    grade = input("Input student grade")

    newStudent = Student(number, name, grade)

    print('New student added:')
    newStudent.printStudentInfo()

    with open("students.txt", "at", newline='') as students:
        wr = csv.writer(students, delimiter=',', quotechar='"')
        wr.writerow([number, name, grade])
    return


def removeStudent():
    number = input('input the student number of the student you want to remove.')

    with open("students.txt", "r") as students:
        lines = students.readlines()
    with open("students.txt", "w") as students:
        for line in lines:
            if not line.startswith(number):
                students.write(line)
    return


def viewChosenCourses():
    print('display your chosen courses')
    return


def chooseCourses():
    print('select 8 courses')
    return


def viewTimetable():
    print('Your timetable: ...')
    return


def changeCourse():
    print('change a course.')
    return


''''
def counsellorMenuWindow():
    window = tk.Tk()

    v = tk.IntVar()

    window.title("Timetabling App")
    window.geometry('1024x512')

    text = tk.Label(window, text='What do you want to do?', fg="red").pack()

    tk.Radiobutton(window, text='View all courses', variable=v, value=1, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Create new course', variable=v, value=2, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Edit a course', variable=v, value=3, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Delete a course', variable=v, value=4, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='View all students', variable=v, value=5, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Add student', variable=v, value=6, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Edit student info', variable=v, value=7, tristatevalue=0).pack(anchor=tk.W)
    tk.Radiobutton(window, text='Remove a student', variable=v, value=8, tristatevalue=0).pack(anchor=tk.W)

    window.mainloop()
    return


mainMenuWindow = tk.Tk()

v = tk.IntVar()

mainMenuWindow.title("Timetabling App")
mainMenuWindow.geometry('1024x512')

textMainMenu = tk.Label(mainMenuWindow, text='Are you are guidance counsellor or a student?', fg="red").pack()

tk.Radiobutton(mainMenuWindow, text='I am a counsellor', variable=v, value=1, tristatevalue=0, command=counsellorMenuWindow) \
    .pack(anchor=tk.W)
tk.Radiobutton(mainMenuWindow, text='I am a student', variable=v, value=2, tristatevalue=0).pack(anchor=tk.W)

mainMenuWindow.mainloop()
'''
# main menu


while True:
    menuChoice = mainMenu()
    if menuChoice == 1:
        # counsellor menu
        while True:
            counsellorMenuChoice = counsellorMenu()
            if counsellorMenuChoice == 1:
                printAllCourses()
            elif counsellorMenuChoice == 2:
                createCourse()
            elif counsellorMenuChoice == 3:
                print('edit courses')
            elif counsellorMenuChoice == 4:
                deleteCourse()
            elif counsellorMenuChoice == 5:
                printAllStudents()
            elif counsellorMenuChoice == 6:
                addStudent()
            elif counsellorMenuChoice == 7:
                print('edit student')
            elif counsellorMenuChoice == 8:
                removeStudent()
            elif counsellorMenuChoice == 9:
                break
    elif menuChoice == 2:
        user = str(input('What is your student number?'))
        while True:
            studentMenuChoice = studentMenu()
            if studentMenuChoice == 1:
                chooseCourses()
            elif studentMenuChoice == 2:
                viewChosenCourses()
            elif studentMenuChoice == 3:
                viewTimetable()
            elif studentMenuChoice == 4:
                changeCourse()
            elif studentMenuChoice == 5:
                break
    elif menuChoice == 3:
        sys.exit()
