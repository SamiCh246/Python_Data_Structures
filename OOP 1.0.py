class Staff:
    def __init__(self, id, t, fn, sn, s):
        self.__staffID = id
        self.__title = t
        self.__firstname = fn
        self.__surname = sn
        self.__salary = s

    def setStaffID(self, id):
        self.__staffID = id

    def setTitle(self, t):
        self.__title = t

    def setFirstname(self, fn):
        self.__firstname = fn

    def setSurname(self, sn):
        self.__surname = sn

    def setSalary(self, s):
        self.__salary = s

    def getStaffID(self):
        return self.__staffID

    def getTitle(self):
        return self.__title

    def getFirstname(self):
        return self.__firstname

    def getSurname(self):
        return self.__surname

    def getSalary(self):
        return self.__salary

    def show(self):
        print('Staff Id: ', self.getStaffID())
        print('Staff Name: ', self.getTitle(), self.getFirstname(), self.getSurname())
        print('Staff Salary: ', self.getSalary())


class Teacher(Staff):  # Teacher class inherits from Staff class
    def __init__(self, id, t, fn, sn, s, fg, cr):
        Staff.__init__(self, id, t, fn, sn, s)
        self.__formGroup = fg
        self.__classRoom = cr

    def setFormGroup(self, fg):
        self.__formGroup = fg

    def setClassroom(self, cr):
        self.__classRoom = cr

    def getFormGroup(self):
        return self.__formGroup

    def getClassRoom(self):
        return self.__classRoom

    def showTeacher(self):
        self.show()
        print('Teacher form group:', self.getFormGroup())
        print('Teacher class room: ', self.getClassRoom())


y = Teacher(1, 'Mr', 'saad', 'malik', 250000, 'A2', 'Lab1')
y.showTeacher()


class SupportStaff(Staff):
    def __init__(self, id, t, fn, sn, s, sts, adp):
        Staff.__init__(self, id, t, fn, sn, s)
        self.__Status = sts
        self.__AcademicDep = adp

    def setStatus(self, sts):
        self.__staffID = sts

    def setAcademicDep(self, adp):
        self.__title = adp

    def getStatus(self):
        return self.__Status

    def getAcademicDep(self):
        return self.__AcademicDep

    def showSupportStaff(self):
        self.show()
        print('Status: ', self.getStatus())
        print('Academic Department: ', self.getAcademicDep())


z = SupportStaff(2, 'Mr', 'Sami', 'Cheema', 2000000, 'part time', 'A2')
z.showSupportStaff()
