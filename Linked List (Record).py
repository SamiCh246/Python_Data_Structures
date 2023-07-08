class Node:
    def __init__(self):
        self.data = ''
        self.ptr = 0


LinkedList = [Node() for i in range(10)]
HeadPtr = -1
FreePtr = 0
CurrentPtr = 0
PreviousPtr = 0


def Initialise():
    for i in range(10):
        LinkedList[i].data = ''
        LinkedList[i].ptr = i + 1
    LinkedList[9].ptr = -1


def Display():
    print('Index', 'Data', 'Pointer')
    for i in range(10):
        print(i, '    ', LinkedList[i].data, '     ', LinkedList[i].ptr)
    print('Head pointer: ', HeadPtr)
    print('Free Pointer: ', FreePtr)


def Insert():
    # sorted list
    global FreePtr, HeadPtr, CurrentPtr, PreviousPtr
    if FreePtr != -1:
        item = input('Enter data: ')
        LinkedList[FreePtr].data = item

        temp = FreePtr
        FreePtr = LinkedList[FreePtr].ptr

        CurrentPtr = HeadPtr
        while CurrentPtr != -1 and LinkedList[CurrentPtr].data < item:
            PreviousPtr = CurrentPtr
            CurrentPtr = LinkedList[CurrentPtr].ptr

        if CurrentPtr == HeadPtr:
            LinkedList[temp].ptr = HeadPtr
            HeadPtr = temp
        else:
            LinkedList[temp].ptr = LinkedList[PreviousPtr].ptr
            LinkedList[PreviousPtr].ptr = temp


def Find(item):
    global CurrentPtr
    CurrentPtr = HeadPtr
    while CurrentPtr != -1 and LinkedList[CurrentPtr].data != item:
        CurrentPtr = LinkedList[CurrentPtr].ptr
    return CurrentPtr


def Delete(item):
    global FreePtr, HeadPtr, PreviousPtr, CurrentPtr
    CurrentPtr = HeadPtr
    while CurrentPtr != -1 and LinkedList[CurrentPtr].data != item:
        PreviousPtr = CurrentPtr
        CurrentPtr = LinkedList[CurrentPtr].ptr

    if CurrentPtr != -1:
        if CurrentPtr == HeadPtr:
            HeadPtr = LinkedList[HeadPtr].ptr
        else:
            LinkedList[PreviousPtr].ptr = LinkedList[CurrentPtr].ptr

    LinkedList[CurrentPtr].ptr = FreePtr
    FreePtr = CurrentPtr


def OutputNodes():
    global CurrentPtr
    CurrentPtr = HeadPtr
    while CurrentPtr != -1:
        print(LinkedList[CurrentPtr].data)
        CurrentPtr = LinkedList[CurrentPtr].ptr


# Main Program
Initialise()
Insert()
Insert()
Insert()
Insert()
Insert()
Delete('e')
Display()
OutputNodes()
