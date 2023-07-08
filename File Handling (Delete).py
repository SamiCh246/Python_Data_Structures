search = str(input('Search: '))
i = 0
search = search+'\n'
file = open('textfile.txt', 'r')
x = file.readline()
file.close()
while len(x) != 0:
    if search != x:
        file = open('textfile.txt', 'w')
        file.write(x)
        file.close()
        i = i + 1
    file = open('textfile.txt', 'r')
    x = file.readline()
file.close()
