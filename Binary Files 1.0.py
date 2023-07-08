import pickle


class Student:
    def __init__(self):
        self.name = ''
        self.marks = 0


x = Student()
file = open('xyz.dat', 'wb')
x.name = input('Enter name: ')
x.marks = int(input('Enter marks: '))
file.seek(5)
pickle.dump(x, file)
file.close()

file = open('xyz.dat', 'rb')
file.seek(5)
y = pickle.load(file)
print(y.name, y.marks)
