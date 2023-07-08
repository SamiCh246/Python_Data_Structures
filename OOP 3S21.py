class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        if int(self.__answer) == answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        if attempts == 2:
            return int(self.__points)//2
        if attempts == 3 or attempts == 4:
            return int(self.__points)//4
        else:
            return 0


def readData():
    global arrayTreasure
    try:
        file = open('TreasureChestData.txt', 'r')
        x = file.readline()
        while x != '':
            question = x
            answer = file.readline()
            points = file.readline()
            arrayTreasure.append(TreasureChest(question, answer, points))
            x = file.readline()
    except EOFError:
        print('file not found')


arrayTreasure = []
Result = False
readData()
questionNo = int(input('Enter Question from 1 to 5: '))
count = 0
while not Result:
    print(arrayTreasure[questionNo - 1].question)
    ans = int(input('Enter Answer: '))
    Result = arrayTreasure[questionNo-1].checkAnswer(ans)
    count = count + 1
print(arrayTreasure[questionNo-1].getPoints(count))
