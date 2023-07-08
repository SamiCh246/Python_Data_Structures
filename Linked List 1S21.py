class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


def outputNodes(List, SPointer):
    CurrentPointer = SPointer
    while CurrentPointer != -1:
        print(List[CurrentPointer].data)
        CurrentPointer = List[CurrentPointer].nextNode


def addNodes(List, SPointer, EPointer):
    Item = int(input('Enter Data to add:'))
    if EPointer < 0 or EPointer > 9:
        return False
    else:
        newNode = node(int(Item), -1)
        List[EPointer] = newNode
        previousPointer = 0
        while SPointer != -1:
            previousPointer = SPointer
            SPointer = List[SPointer].nextNode
        List[previousPointer].nextNode = EPointer
        EPointer = List[EPointer].nextNode
        return True


LinkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3),
              node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5
addNodes(LinkedList, startPointer, emptyList)
outputNodes(LinkedList, startPointer)
