class Staff:
    def __init__(self, id, t, fn, sn, s, lc):
        self.__staffID = id
        self.__name = Name(t, fn, sn)
        self.__salary = s
        self.__LunchCost = lc

    def setStaffID(self, id):
        self.__staffID = id

    def setName(self, t, fn, sn):
        self.__name = Name(t, fn, sn)

    def setSalary(self, s):
        self.__salary = s

    def setLunchCost(self, lc):
        self.__LunchCost = lc

    def getStaffID(self):
        return self.__staffID

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getLunchCost(self):
        return self.__LunchCost

    def show(self):
        print('Staff Id: ', self.getStaffID())
        print('Staff name: ', self.__name.showName('1'))
        print('Staff Salary: ', self.getSalary())
        print('Lunch Cost: ', self.getLunchCost())


class Name:
    def __init__(self, t, fn, sn):
        self.__title = t
        self.__firstname = fn
        self.__surname = sn

    def setTitle(self, t):
        self.__title = t

    def setFirstname(self, fn):
        self.__firstname = fn

    def setSurname(self, sn):
        self.__surname = sn

    def getTitle(self):
        return self.__title

    def getFirstname(self):
        return self.__firstname

    def getSurname(self):
        return self.__surname

    def showName(self, opt):
        if opt == '1':
            return self.getTitle() + ' ' + self.getFirstname() + ' ' + self.getSurname()
        if opt == '2':
            return self.getSurname() + ' ' + self.getFirstname()


class Teacher(Staff):  # Teacher class inherits from Staff class
    def __init__(self, id, t, fn, sn, s, lc, fg, cr):
        Staff.__init__(self, id, t, fn, sn, s, lc)
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


class SupportStaff(Staff):
    def __init__(self, id, t, fn, sn, s, lc, sts, adp):
        Staff.__init__(self, id, t, fn, sn, s, lc)
        self.__Status = sts
        self.__AcademicDep = adp

    def setStatus(self, sts):
        self.__staffID = sts

    def setAcademicDep(self, adp):
        self.__AcademicDep = adp

    def getStatus(self):
        return self.__Status

    def getAcademicDep(self):
        return self.__AcademicDep

    def showSupportStaff(self):
        self.show()
        print('Status: ', self.getStatus())
        print('Academic Department: ', self.getAcademicDep())


print('---------------------------')
LC = 300000*(1/8)
x = Staff(2, 'Mr', 'Faheem', 'Ijaz', 300000, LC)
x.show()
print('---------------------------')
LC = 250000*(1/8)
y = Teacher(1, 'Mr', 'saad', 'malik', 250000, LC, 'A2', 'Lab1')
y.showTeacher()
print('---------------------------')
LC = 200000*(1/8)
z = SupportStaff(2, 'Mr', 'Sami', 'Cheema', 200000, LC, 'part time', 'A2')
z.showSupportStaff()
print('---------------------------')
n = Name('Mr', 'Haroon', 'Maqbool')
print(n.showName('2'))
print('---------------------------')
