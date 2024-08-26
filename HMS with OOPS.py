                                    # Hospital Management System

# BLL: Business Logic Layer

class Employee:
    emp_list = []
    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.mob = 0
        self.city=0
        self.state=0
        self.address=0

    def addemployee(self):
        Employee.emp_list.append(self)

    def searchemployee(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.state= e.state
                self.city=e.city
                self.address=e.address
                return

    def deleteemployee(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)

    def modifyemployee(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.state=self.state
                e.city=self.city
                e.address=self.address
                return


class Patient(Employee):
    def __init__(self):
        self.gender=0
        self.weight=0
        self.height=0
        self.Date=0
        self.BirthOfDate=0
        self.InsuranceCompanyName=0
        self.PolicyNumber=0
        super().__init__()

    def addpatient(self):
        Employee.emp_list.append(self)

    def searchpatient(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.state = e.state
                self.city=e.city
                self.address=e.address
                self.gender=e.gender
                self.weight=e.weight
                self.height=e.height
                self.Date=e.Date
                self.BirthOfDate=e.BirthOfDate
                self.InsuranceCompanyName=e.InsuranceCompanyName
                self.PolicyNumber=e.PolicyNumber
                return

    def deletepatient(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)
            Employee.emp_list.pop()

    def modifypatient(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.state = self.state
                e.city=self.city
                e.address=self.address
                e.gender=self.gender
                e.weight=self.weight
                e.height=self.height
                e.Date=self.Date
                e.BirthOfDate=self.BirthOfDate
                e.InsuranceCompanyName=self.InsuranceCompanyName
                e.PolicyNumber=self.PolicyNumber
                return


class Doctor(Employee):
    def __init__(self):
        self.specialist = 0
        super().__init__()

    def adddoctor(self):
        Employee.emp_list.append(self)

    def searchdoctor(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.state = e.state
                self.city=e.city
                self.address=e.address
                self.specialist=e.specialist
                return

    def deletedoctor(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)
            Employee.emp_list.pop()

    def modifydoctor(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.state = self.state
                e.city=self.city
                e.address=self.address
                e.specialist=self.specialist
                return


class Director(Employee):
    def __init__(self):
        self.share = 0
        super().__init__()

    def adddirector(self):
        Employee.emp_list.append(self)

    def searchdirector(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name = e.name
                self.age = e.age
                self.mob = e.mob
                self.address=e.address
                self.state=e.state
                self.city=e.city
                self.share = e.share
                return

    def deletedirector(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)
            Employee.emp_list.pop()

    def modifydirector(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.address=self.address
                e.state=self.state
                e.city=self.city
                e.share = self.share
                return


# PL: Presentation Layer

print("Welcome To Hospital Management System")


def showEmployee(emp):
    print("EMP ID:", emp.id, "EMP NAME:", emp.name, "EMP AGE:", emp.age, "EMP MOB:", emp.mob, "EMP ADDRESS:", emp.address, "EMP STATE:", emp.state, "EMP CITY:", emp.city)

def showPatient(pat):
    print("PAT ID:", pat.id, "PAT NAME:", pat.name, "PAT AGE:", pat.age, "PAT MOB:", pat.mob, "PAT ADDRESS:", pat.address,
          "PAT STATE:", pat.state, "PAT city:", pat.city, "PAT GENDER:", pat.gender,"PAT WEIGHT:", pat.weight,
          "PAT HEIGHT:", pat.height, "PAT DATE:", pat.Date,"PAT DATE OF BIRTH:", pat.BirthOfDate,
          "PAT INSURANCE COMPANY NAME:", pat.InsuranceCompanyName, "PAT POLICY NUMBER:", pat.PolicyNumber)


def showDoctor(dor):
    print("DOR ID:", dor.id, "DOR NAME:", dor.name, "DOR AGE:", dor.age, "DOR MOB:", dor.mob, "DOR ADDRESS:", dor.address, "DOR STATE:", dor.state, "DOR CITY:", dor.city)


def showDirector(dir):
    print("DIR ID:", dir.id, "DIR NAME:", dir.name, "DIR AGE:", dir.age, "DIR MOB:", dir.mob, "DIR ADDRESS:", dir.address, "DIR STATE:", dir.state, "DIR CITY:", dir.city, "DIR SHARE:", dir.share)


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
    ch = input("Enter choice: 1 ADD EMPLOYEE, 2 PATIENT, 3 DOCTOR, 4 DIRECTOR, 5 EXIT:")

    # EMPLOYEE

    if (ch == ("1")):
        while (1):
            ch = input("Enter choice: 1 ADD EMPLOYEE, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                emp = Employee()
                emp.id = input("Enter the employee ID:")
                emp.name = input("Enter the employee NAME:")
                emp.age = input("Enter the employee AGE:")
                emp.state = input("Enter the employee STATE:")
                emp.city = input("Enter the employee CITY:")
                emp.address = input("Enter the employee ADDRESS:")
                emp.mob = getmob()
                emp.addemployee()
            elif (ch == "2"):
                emp = Employee()
                emp.id = input("Enter the employee ID:")
                emp.searchemployee()
                showEmployee(emp)
            elif (ch == "3"):
                emp = Employee()
                emp.id = input("Enter the employee ID:")
                emp.deleteemployee()
                showEmployee(emp)
            elif (ch == "4"):
                emp = Employee()
                emp.id = input("Enter the update employee ID:")
                emp.name = input("Enter the update employee NAME:")
                emp.age = input("Enter the update employee AGE:")
                emp.state = input("Enter the update employee STATE:")
                emp.city = input("Enter the update employee CITY:")
                emp.address = input("Enter the update employee ADDRESS:")
                emp.modifyemployee()
                emp.mob = getmob()
            elif (ch == "5"):
                for i in Employee.emp_list:
                    showEmployee(i)
            elif (ch == "6"):
                print("Thanks for using Hospital Employee Department")
                break
            else:
                print("invalid choice")

    # PATIENT

    if (ch == "2"):
        while (1):
            ch = input("Enter choice: 1 ADD PATIENT, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                pat = Patient()
                pat.id = input("Enter the patient ID:")
                pat.name = input("Enter the patient NAME:")
                pat.age = input("Enter the patient AGE:")
                pat.address = input("Enter the patient ADDRESS :")
                pat.state = input("Enter the patient STATE:")
                pat.city = input("Enter the patient CITY:")
                pat.gender = input("Enter the patient GENDER:")
                pat.weight = input("Enter the patient WEIGHT:")
                pat.height = input("Enter the patient HEIGHT:")
                pat.Date = input("Enter the patient DATE:")
                pat.BirthOfDate = input("Enter the patient BIRTH OF DATE:")
                pat.InsuranceCompanyName = input("Enter the patient INSURANCE COMPANY NAME:")
                pat.PolicyNumber = input("Enter the patient POLICY NUMBER:")
                pat.mob = getmob()

                pat.addpatient()
            elif (ch == "2"):
                pat = Patient()
                pat.id = input("Enter the patient ID:")
                pat.searchpatient()
                showPatient(pat)
            elif (ch == "3"):
                pat = Patient()
                pat.id = input("Enter the patient ID:")
                pat.deletepatient()
                showPatient(pat)
            elif (ch == "4"):
                pat = Patient()
                pat.id = input("Enter the update patient ID:")
                pat.name = input("Enter the update patient NAME:")
                pat.age = input("Enter the update patient AGE:")
                pat.address = input("Enter the update patient ADDRESS:")
                pat.state = input("Enter the update patient STATE:")
                pat.city = input("Enter the update patient CITY:")
                pat.gender = input("Enter the update patient GENDER:")
                pat.weight = input("Enter the update patient HEIGHT:")
                pat.height = input("Enter the update patient WEIGHT:")
                pat.Date = input("Enter the update patient DATE:")
                pat.BirthOfDate = input("Enter the update patient BIRTH OF DATE:")
                pat.InsuranceCompanyName = input("Enter the update patient INSURANCE COMPANY NAME:")
                pat.PolicyNumber = input("Enter the update patient POLICY NUMBER:")
                pat.mob = getmob()
                pat.modifypatient()
            elif (ch == "5"):
                for i in Patient.emp_list:
                    showPatient(i)
            elif (ch == "6"):
                print("Thanks for using Hospital Patient Department")
                break
            else:
                print("invalid choice")

    # DOCTOR

    if (ch == "3"):
        while (1):
            ch = input("Enter choice: 1 ADD DOCTOR, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
                dor = Doctor()
                dor.id = input("Enter the doctor ID:")
                dor.name = input("Enter the doctor NAME:")
                dor.age = input("Enter the doctor AGE:")
                dor.address = input("Enter the doctor ADDRESS:")
                dor.state = input("Enter the doctor STATE:")
                dor.city = input("Enter the doctor CITY:")
                dor.mob = getmob()
                dor.specialist = input("Enter the dor SPECIALIST:")
                dor.adddoctor()
            elif (ch == "2"):
                dor = Doctor()
                dor.id = input("Enter the doctor ID:")
                dor.searchdoctor()
                showDoctor(dor)
            elif (ch == "3"):
                dor = Doctor()
                dor.id = input("Enter the doctor ID:")
                dor.deletedoctor()
            elif (ch == "4"):
                dor = Doctor()
                dor.id = input("Enter the update doctor ID:")
                dor.name = input("Enter the update doctor NAME:")
                dor.age = input("Enter the update doctor AGE:")
                dor.address = input("Enter the update doctor ADDRESS:")
                dor.state = input("Enter the update doctor STATE:")
                dor.city = input("Enter the update doctor CITY:")
                dor.mob = getmob()
                dor.specialist = input("Enter the update doctor SPECIALIST:")
                dor.modifydoctor()
            elif (ch == "5"):
                for i in Doctor.emp_list:
                    showDoctor(i)
            elif (ch == "6"):
                print("Thanks for using Hospital Doctors Department")
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
                dir.state = input("Enter the director STATE:")
                dir.city = input("Enter the director CITY:")
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
                dir.state = input("Enter the update director STATE:")
                dir.city = input("Enter the update director CITY:")
                dir.mob = getmob()
                dir.share = input("Enter the update director SHARE:")
                dir.modifydirector()
            elif (ch == "5"):
                for i in Director.emp_list:
                    showDirector(i)
            elif (ch == "6"):
                print("Thanks for using Hospital Directors Department")
                break
    elif (ch == "5"):
        print("Thanks For Using Hospital Management system")
        break
    else:
        print("Invalid choice")





