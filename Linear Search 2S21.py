def LinearSearch(Int):
    global arrayData
    index = 0
    Found = False
    while index < len(arrayData):
        if arrayData[index] == Int:
            Found = True
            return Found
        index = index + 1
    if not Found:
        return Found


arrayData = [0] * 10
arrayData[0] = 10
arrayData[1] = 5
arrayData[2] = 6
arrayData[3] = 7
arrayData[4] = 1
arrayData[5] = 12
arrayData[6] = 13
arrayData[7] = 15
arrayData[8] = 21
arrayData[9] = 8

Integer = int(input('Enter value to search: '))
LinearSearch(Integer)
if LinearSearch(Integer):
    print('Search value found')
else:
    print('Search value not found')
