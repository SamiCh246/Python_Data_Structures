file = open('textfile.txt', 'r')
x = file.readline().strip()
while len(x) != 0:
    print(x)
    x = file.readline().strip()
file.close()
