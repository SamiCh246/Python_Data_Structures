QueueData = [''] * 20
startPointer = 0
endPointer = -1


def Enqueue(Item):
    global startPointer, endPointer
    if endPointer < 9:
        endPointer = endPointer + 1
        QueueData[endPointer] = Item
        return True
    else:
        return False


def ReadFile():
    Found = True
    filename = input('Enter file Name: ')
    try:
        file = open(filename, 'r')
        x = file.readline().strip()
        while len(x) != 0 and Found:
            if Enqueue(x):
                x = file.readline().strip()
            else:
                Found = False
        if not Found:
            return 2
        else:
            return 1
    except IOError:
        return -1


def Remove():
    global startPointer, endPointer
    DataRemove = ''
    Removed = False
    if endPointer >= 1 and not Removed:
        for i in range(2):
            if i == 0:
                DataRemove = DataRemove + QueueData[startPointer]
            else:
                DataRemove = DataRemove + ' ' + QueueData[startPointer]
            QueueData[startPointer] = ''
            startPointer = startPointer + 1
        Removed = True
    else:
        return 'No Items'
    print(DataRemove)


Result = ReadFile()
if Result == 1:
    print('all items are added to the queue')
elif Result == 2:
    print('the queue was full')
elif Result == -1:
    print('the text file could not be found')
Remove()
