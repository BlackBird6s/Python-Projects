                                  # School Management System using with OOPS
# BLL: Business Logic Layer

class SchoolStaff:
    stf_list = []

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0
        self.address = 0
        self.salary = 0

    def addstaff(self):
        SchoolStaff.stf_list.append(self)

    def searchstaff(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                self.name = id.name
                self.age = id.age
                self.mob = id.mob
                self.address=id.address
                self.salary=id.salary
                return

    def deletestaff(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                SchoolStaff.stf_list.remove(e)
        SchoolStaff.stf_list.pop()

    def modifystaff(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address = self.address
                e.salary = self.salary
                return


class Student(SchoolStaff):
    def __init__(self):
        self.fathername = 0
        self.mothername = 0
        self.Class = 0
        self.Section = 0
        super().__init__()

    def addstudent(self):
        SchoolStaff.stf_list.append(self)

    def searchstudent(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.address = e.address
                self.fathername = e.fathername
                self.mothername = e.mothername
                self.Class = e.Class
                self.section = e.section
                return

    def deletestudent(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                SchoolStaff.stf_list.remove(e)
            SchoolStaff.stf_list.pop()

    def modifystudent(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address = self.address
                e.fathername = self.fathername
                e.mothername = self.mothername
                e.Class = self.Class
                e.section = self.section
                return


class Teacher(SchoolStaff):
    def __init__(self):
        self.subject = 0
        self.salary = 0
        super().__init__()

    def addteacher(self):
        SchoolStaff.stf_list.append(self)

    def searchteacher(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.address = e.address
                self.subject = e.subject
                self.salary = e.salary
                return

    def deleteteacher(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                SchoolStaff.stf_list.remove(e)
            SchoolStaff.stf_list.pop()

    def modifyteacher(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address = self.address
                e.subject = self.subject
                e.salary = self.salary
                return


class Director(SchoolStaff):
    def __init__(self):
        self.share = 0
        super().__init__()

    def adddirector(self):
        SchoolStaff.stf_list.append(self)

    def searchdirector(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.address = e.address
                self.share = e.share
                return

    def deletedirector(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                SchoolStaff.stf_list.remove(e)
            SchoolStaff.stf_list.pop()

    def modifydirector(self):
        for e in SchoolStaff.stf_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address = self.address
                e.share = self.share
                return


# PL: Presentation Layer

print("Welcome to SMS with OOPS")


def showSchoolStaff(stf):
    print("STF ID:", stf.id, "STF NAME:", stf.name, "STF AGE:", stf.age, "STF MOB:", stf.mob, "STF ADDRESS:", stf.address, "STF SALARY:", stf.salary)


def showStudent(std):
    print("STD ID:", std.id, "STD NAME:", std.name, "STD AGE:", std.age, "STD MOB:", std.mob, "STD FATHER NAME:", std.fathername, "STD MOTHER NAME:", std.mothername, "STD CLASS:", std.Class, "STD SECTION:", std.Section)


def showTeacher(tea):
    print("TEA ID:", tea.id, "TEA NAME:", tea.name, "TEA AGE:", tea.age, "TEA MOB:", tea.mob, "TEA COURSE:", tea.subject,"STF SALARY:", stf.salary)


def showDirector(dir):
    print("DIR ID:", dir.id, "DIR NAME:", dir.name, "DIR AGE:", dir.age, "DIR MOB:", dir.mob, "DIR SHARE:", dir.share)


def getmob():
    while (1):
        mob = input("Enter mob number:")
        if (mob.isdecimal()):
            if (len(mob) == 10):
                return mob
            else:
                print("Enter the number for 10 digits")
        else:
            print("Enter mob no's with digits only")


while (1):
    ch = input("Enter choice: 1 ADD SCHOOL STAFF, 2 STUDENT, 3 TEACHER, 4 DIRECTOR, 5 EXIT:")

# SCHOOL STAFF

    if (ch == ("1")):
        while (1):
            ch = input("Enter choice: 1 ADD SCHOOL STAFF, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                stf = SchoolStaff()
                stf.id = input("Enter the staff ID:")
                stf.name = input("Enter the staff NAME:")
                stf.age = input("Enter the staff AGE:")
                stf.address = input("Enter the staff ADDRESS:")
                stf.salary = input("Enter the staff SALARY:")
                stf.mob = getmob()
                stf.addstaff()
            elif (ch == "2"):
                stf = SchoolStaff()
                stf.id = input("Enter the staff ID:")
                stf.searchstaff()
                showSchoolStaff(stf)
            elif (ch == "3"):
                stf = SchoolStaff()
                stf.id = input("Enter the staff ID:")
                stf.deletestaff()
                showSchoolStaff(stf)
            elif (ch == "4"):
                stf = SchoolStaff()
                stf.id = input("Enter the update staff ID:")
                stf.name = input("Enter the update staff NAME:")
                stf.age = input("Enter the update staff AGE:")
                stf.address = input("Enter the update staff ADDRESS:")
                stf.salary = input("Enter the update staff SALARY:")
                stf.mob = getmob()
            elif (ch == "5"):
                for i in SchoolStaff.stf_list:
                    showSchoolStaff(i)
            elif (ch == "6"):
                print("Thanks for using School Staff Department")
                break
            else:
                print("invalid choice")

# STUDENT

    if (ch == "2"):
        while (1):
            ch = input("Enter choice: 1 ADD STUDENT, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                std = Student()
                std.id = input("Enter the student ID:")
                std.name = input("Enter the student NAME:")
                std.age = input("Enter the student AGE:")
                std.address = input("Enter the student ADDRESS:")
                std.mob = getmob()
                std.fathername = input("Enter the student FATHER NAME:")
                std.mothername = input("Enter the student MOTHER NAME:")
                std.Class = input("Enter the student CLASS:")
                std.Section = input("Enter the student SECTION:")
                std.addstudent()
            elif (ch == "2"):
                std = Student()
                std.id = input("Enter the student ID:")
                std.searchstudent()
                showStudent(std)
            elif (ch == "3"):
                std = Student()
                std.id = input("Enter the manager ID:")
                std.deletestudent()
                showStudent(std)
            elif (ch == "4"):
                std = Student()
                std.id = input("Enter the update student ID:")
                std.name = input("Enter the update student NAME:")
                std.age = input("Enter the update student AGE:")
                std.address = input("Enter the update student ADDRESS:")
                std.mob = getmob()
                std.fathername = input("Enter the update student FATHER NAME:")
                std.mothername = input("Enter the update student MOTHER NAME:")
                std.Class = input("Enter the student update CLASS:")
                std.Section = input("Enter the student update SECTION:")
                std.modifystudent()
            elif (ch == "5"):
                for i in Student.stf_list:
                    showStudent(i)
            elif (ch == "6"):
                print("Thanks for using Student Department")
                break
            else:
                print("invalid choice")

# TEACHER

    if (ch == "3"):
        while (1):
            ch = input("Enter choice: 1 ADD Teacher, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                tea = Teacher()
                tea.id = input("Enter the teacher ID:")
                tea.name = input("Enter the teacher NAME:")
                tea.age = input("Enter the teacher AGE:")
                tea.address = input("Enter the teacher ADDRESS:")
                tea.salary = input("Enter the teacher SALARY:")
                tea.mob = getmob()
                tea.subject = input("Enter the teacher SUBJECT:")
                tea.addteacher()
            elif (ch == "2"):
                tea = Teacher()
                tea.id = input("Enter the teacher ID:")
                tea.searchteacher()
                showTeacher(tea)
            elif (ch == "3"):
                tea = Teacher()
                tea.id = input("Enter the teacher ID:")
                tea.deleteteacher()
            elif (ch == "4"):
                tea = Teacher()
                tea.id = input("Enter the update trainer ID:")
                tea.name = input("Enter the update trainer NAME:")
                tea.age = input("Enter the update trainer AGE:")
                tea.address = input("Enter the update teacher ADDRESS:")
                tea.salary = input("Enter the update teacher SALARY:")
                tea.mob = getmob()
                tea.course = input("Enter the update teacher SUBJECT:")
                tea.modifyteacher()
            elif (ch == "5"):
                for i in Teacher.stf_list:
                    showTeacher(tea)
            elif (ch == "6"):
                print("Thanks for using Teacher Department")
                break
            else:
                print("invalid choice")

# DIRECTOR

    if (ch == "4"):
        while (1):
            ch = input("Enter choice: 1 ADD DIRECTOR, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                dir = Director()
                dir.id = input("Enter the director ID:")
                dir.name = input("Enter the director NAME:")
                dir.age = input("Enter the director AGE:")
                dir.address = input("Enter the director ADDRESS:")
                dir.mob = getmob()
                dir.share = input("Enter the director SHARE:")
                dir.adddirector()
            elif (ch == "2"):
                dir = Director()
                dir.id = input("Enter the director ID:")
                dir.searchdirector()
                showDirector(dir)
            elif (ch == "3"):
                dir = Director()
                dir.id = input("Enter the director ID:")
                dir.deletedirector()
            elif (ch == "4"):
                dir = Director()
                dir.id = input("Enter the update director ID:")
                dir.name = input("Enter the update director NAME:")
                dir.age = input("Enter the update director AGE:")
                dir.address = input("Enter the update director ADDRESS:")
                dir.mob = getmob()
                dir.share = input("Enter the update director SHARE:")
                dir.modifydirector()
            elif (ch == "5"):
                for i in Director.stf_list:
                    showDirector(i)
            elif (ch == "6"):
                print("Thanks for using School directors Department")
                break
    elif (ch == "5"):
        print("thanks for using SMS with OOPS")
        break
    else:
        print("Invalid choice")





