def Binary_Sort(List, N):
    LowerBound = N
    Top = LowerBound
    while True:
        Swap = False
        for index in range(Top-1):
            if List[index] > List[index+1]:
                Temp = List[index]
                List[index] = List[index+1]
                List[index+1] = Temp
                Swap = True
        if not Swap:
            break
    print(List)


NElements = int(input('No. of Names: '))
MyList = [""] * NElements
for i in range(NElements):
    MyList[i] = input('Input Name:')
Binary_Sort(MyList, NElements)
