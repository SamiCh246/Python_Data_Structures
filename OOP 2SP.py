class HiddenBox:
    # BoxName : string
    # Creator : string
    # DateHidden : string
    # GameLocation : string
    # LastFinds : [10] [2] string
    # Active : string
    def __init__(self, bn, cr, dh, gl):
        self.__BoxName = bn
        self.__Creator = cr
        self.__DateHidden = dh
        self.__GameLocation = gl
        self.__LastFinds = [["" for i in range(0, 2)] for j in range(0, 10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


class PuzzleBox(HiddenBox):
    def __init__(self, bn, cr, dh, gl, pt, sl):
        HiddenBox.__init__(self, bn, cr, dh, gl)
        self.__PuzzleText = pt
        self.__Solution = sl


def NewBox():
    Name = str(input('Input Name: '))
    Creator = str(input('Input Creator: '))
    DateHidden = str(input('Input Date Hidden: '))
    GameLocation = str(input('Input Game Location: '))
    TheBoxes.append(HiddenBox(Name, Creator, DateHidden, GameLocation))


TheBoxes = [HiddenBox('', '', '', '') for i in range(10000)]
NewBox()
