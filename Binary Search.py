def Binary_Search(List, N):
    UpperBound = 0
    LowerBound = N
    Position = 0
    Found = False
    Search = str(input('Search Name: '))
    while LowerBound != UpperBound or not Found:
        MidPoint = (UpperBound+LowerBound)//2
        if List[MidPoint] == Search:
            Found = True
            Position = MidPoint
            break
        elif List[MidPoint] > Search:
            UpperBound = UpperBound - 1
        else:
            LowerBound = LowerBound + 1
    if Found:
        print('Name found at: ', Position)
    else:
        print('Name not found')


NElements = int(input('No. of Names: '))
MyList = [""] * NElements
for i in range(NElements):
    MyList[i] = input('Input Name:')
Binary_Search(MyList, NElements)
