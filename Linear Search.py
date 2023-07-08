def Linear_Search(List, N):
    index = 0
    Found = False
    Position = 0
    Search = str(input('Search Name: '))
    while index != N+1 or not Found:
        if List[index] == Search:
            Found = True
            Position = index
            break
        else:
            index = index + 1
    if Found:
        print('Name found at: ', Position)
    else:
        print('Name not found')


NElements = int(input('No. of Names: '))
MyList = [""] * NElements
for i in range(NElements):
    MyList[i] = input('Input Name:')
Linear_Search(MyList, NElements)
