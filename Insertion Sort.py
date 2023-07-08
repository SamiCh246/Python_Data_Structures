def Insertion_Sort(ListA):
    for count in range(1, len(ListA)):
        DataToInsert = ListA[count]
        Inserted = False
        NextValue = count - 1
        while NextValue >= 0 and not Inserted:
            if DataToInsert < ListA[NextValue]:
                ListA[NextValue + 1] = ListA[NextValue]
                NextValue = NextValue - 1
                ListA[NextValue + 1] = DataToInsert
            else:
                Inserted = True


NElements = int(input('No. of Names: '))
MyList = [""] * NElements
for i in range(NElements):
    MyList[i] = input('Input Name:')
Insertion_Sort(MyList)
print(MyList)
