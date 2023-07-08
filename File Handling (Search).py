search = str(input('Search: '))
search = search+'\n'
Found = False
file = open('textfile.txt', 'r')
x = file.readline()
while len(x) != 0:
    if search == x:
        Found = True
        break
    x = file.readline()
file.close()
if Found:
    print('Record Found')
else:
    print('Not Found')
