def Menu():
    print('1. Push')
    print('2. Pop')
    print('3. End')
    option = int(input('Select any number: '))
    if option == 1:
        Push()
    elif option == 2:
        Pop()
    elif option == 3:
        exit()
    print(Stack)
    Menu()


def Push():
    global Stackpointer
    string = str(input('Input String:'))
    if Stackpointer == 9:
        print('Stack is full')
    else:
        Stackpointer = Stackpointer + 1
        Stack[Stackpointer] = string


def Pop():
    global Stackpointer
    if Stackpointer == -1:
        print('Stack is empty')
    else:
        Stack[Stackpointer] = ''
        Stackpointer = Stackpointer - 1


Stack = ['']*10
Stackpointer = -1
Menu()
