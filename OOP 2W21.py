class Picture:
    def __init__(self, description, width, height, frColour):
        self.__description = description
        self.__width = width
        self.__height = height
        self.__frColour = frColour

    def GetDescription(self):
        return self.__description

    def GetWidth(self):
        return int(self.__width)

    def GetHeight(self):
        return int(self.__height)

    def GetFrColour(self):
        return str(self.__frColour)

    def SetDescription(self, description):
        self.__description = description


def ReadData():
    global PArray
    file = open('Pictures.txt', 'r')
    index = 0
    x = file.readline()
    try:
        while len(x) != 0:
            description = x.strip()
            width = file.readline().strip()
            height = file.readline().strip()
            frColour = file.readline().strip()
            Pic = Picture(description, width, height, frColour)
            PArray[index] = Pic
            index = index + 1
            x = file.readline()
    except IOError:
        print('File not found')
    count = index + 1
    return count


PArray = []
for i in range(100):
    PArray.append(Picture("", 0, 0, ""))
ReadData()
Found = False
FrameC = input('Enter frame colour: ')
MaxW = int(input('Enter maximum width: '))
MaxH = int(input('Enter maximum height: '))
for i in range(100):
    if (FrameC.lower() == PArray[i].GetFrColour()) and (PArray[i].GetWidth() <= MaxW) and PArray[i].GetHeight() <= MaxH:
        Found = True
        print(PArray[i].GetDescription(), PArray[i].GetWidth(), PArray[i].GetHeight())
if not Found:
    print('Picture not found')
