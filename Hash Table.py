class CustomerRecord:
    def __init__(self):
        self.username = ''
        self.purchase = 0


CustomerList = [CustomerRecord() for i in range(5)]


def Menu():
    print('1. Insert')
    print('2. Search')
    print('3. Output')
    print('4. Initialise')
    print('5. Exit')
    Option = int(input('Choose Option: '))
    if Option == 1:
        Insert()
    elif Option == 2:
        Search()
    elif Option == 3:
        Output()
    elif Option == 4:
        Initialise()
    elif Option == 5:
        exit()
    Menu()


def Initialise():
    for i in range(5):
        CustomerList[i].username = ''
        CustomerList[i].purchase = 0


def Hash(Username):
    tASCII = 0
    for i in range(len(Username)):
        tASCII = tASCII + ord(Username[i])
    address = tASCII % 5
    return address


def Insert():
    if Check_Empty():
        Name = str(input('Enter name: '))
        Purchase = int(input('Enter amount of purchase: '))
        index = Hash(Name)
        while CustomerList[index].username != '':
            index = index + 1
            if index == 30:
                index = 0
        CustomerList[index].username = Name
        CustomerList[index].purchase = Purchase
    else:
        print('List if Full')


def Check_Empty():
    Found = False
    for index in range(len(CustomerList)):
        if CustomerList[index].username == '':
            Found = True
    if Found:
        return True
    else:
        return False


def Search():
    Found = False
    SearchItem = str(input('Input Search Item: '))
    HSearch = Hash(SearchItem)
    for index in range(len(CustomerList)):
        if Hash(CustomerList[index].username) == HSearch:
            Found = True
            print('Found at: ', index)
    if not Found:
        print('Item Not found')


def Output():
    for i in range(len(CustomerList)):
        print(CustomerList[i].username, '-', CustomerList[i].purchase)


Menu()
