import pickle


class Student:
    def __init__(self):
        self.name = ''
        self.marks = 0


Students = [Student() for i in range(10)]


def Insert():
    file2 = open('MyFile.dat', 'wb')
    for i in range(2):
        index = int(input('Enter Address: '))
        Students[index].name = input('Enter Name: ')
        Students[index].marks = int(input('Enter Marks: '))
        file2.seek(index)
        pickle.dump(Students[index], file2)
    file2.close()


def LoadData():
    try:
        file2 = open('MyFile.dat', 'rb')
        for i in range(10):
            file2.seek(i)
            Students[i] = pickle.load(file2)
        file2.close()
    except:
        pass


def PrintAll():
    for i in range(10):
        print(Students[i].name, Students[i].marks)


Insert()
LoadData()
PrintAll()
