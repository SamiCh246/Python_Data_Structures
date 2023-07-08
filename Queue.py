def Menu():
    print('1. Enqueue')
    print('2. Dequeue')
    print('3. End')
    Option = int(input('Select any number: '))
    if Option == 1:
        Enqueue()
    elif Option == 2:
        Dequeue()
    elif Option == 3:
        exit()
    print(Queue)
    Menu()


def Enqueue():
    global Frontpointer
    global Rearpointer
    if Rearpointer <= 8:
        String = str(input('Input String:'))
        Rearpointer = Rearpointer + 1
        Queue[Rearpointer] = String
    else:
        print('Queue is full')


def Dequeue():
    global Frontpointer
    global Rearpointer
    if Frontpointer <= Rearpointer:
        Queue[Frontpointer] = ''
        Frontpointer = Frontpointer + 1
    else:
        print('Queue is empty')


Queue = [''] * 10
Frontpointer = 0
Rearpointer = -1
Menu()
