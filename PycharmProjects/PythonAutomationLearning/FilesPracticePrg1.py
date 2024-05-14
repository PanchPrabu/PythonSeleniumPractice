with open('readwritepractice1.txt', 'w') as w1:
    w1.write("Programming with Python is Fun.\nLet's try.")
with open('readwritepractice1.txt', 'r') as R1:
    #print(R1.read())
    #print(R1.readlines())
    countlines = 0
    for line in R1.readlines():
        countlines += countlines + 1
    print("The number of lines in the file is", countlines)
    print("The file name is :",R1.name)
