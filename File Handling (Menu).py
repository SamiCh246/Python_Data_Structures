def menu():
    print('1. Write to File')
    print('2. Append to File')
    print('3. Search for Item')
    print('4. Search for a keyword in the descriptions')
    print('5. End')
    c = int(input('Key in choice'))
    if c == 1:
        Write()
    elif c == 2:
        Append()
    elif c == 3:
        SearchByTerm()
    elif c == 4:
        SearchDescriptionsForKeyword()
    elif c == 5:
        exit()
    menu()


def Write():
    file = open('MyFile.txt', 'w')
    x = str(input('Enter Text to Write'))
    file.write(x)
    file.write('\n')
    file.close()


def Append():
    file = open('MyFile.txt', 'a')
    x = str(input('Enter Text to Write'))
    file.write(x)
    file.write('\n')
    file.close()


def SearchByTerm():
    file = open('MyFile.txt', 'r')
    search = input('Enter Item to Search')
    x = file.readline()
    found = False
    while len(x) != 0:
        if search in x:
            found = True
            x = file.readline()
            print(x)
        x = file.readline()
    if not found:
        print("Term Not found")
    file.close()


def SearchDescriptionsForKeyword():
    index = 0
    file = open('MyFile.txt', 'r')
    search = input('Enter Keyword')
    x = file.readline()
    found = False
    while len(x) != 0:
        if search in x:
            found = True
            index = index+1
            lowerbound = index - 1
            upperbound = index
            file = open('MyFile.txt', 'r')
            for i in range(index):
                x = file.readline()
                if index == lowerbound or index == upperbound:
                    print(x)
        x = file.readline()
    if not found:
        print("Term Not found")
    file.close()


menu()
