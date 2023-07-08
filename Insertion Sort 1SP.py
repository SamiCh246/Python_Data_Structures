def InsertionSort(ListA):
    for count in range(1, len(ListA)):
        DataToInsert = ListA[count]
        Inserted = 0
        NextValue = count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


def OutputData(ListA):
    for i in range(len(ListA)):
        print(ListA[i])


def SearchData(ListA):
    found = False
    Number = int(input('Enter a whole number: '))
    for i in range(len(ListA)):
        if ListA[i] == Number:
            found = True
            return found
    if not found:
        return found


TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
print('Data before sorting:')
OutputData(TheData)
InsertionSort(TheData)
print('Data after sorting:')
OutputData(TheData)
print(SearchData(TheData))
