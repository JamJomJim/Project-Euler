def parseNum(filename, shouldprint):
    numbergrid = open(filename)
    read = False
    numarray = []
    while not read:
        curline = numbergrid.readline()
        if curline == "":
            break
        numarray.append(curline.split(' '))
    for i in range(len(numarray)):
        if "\n" in numarray[i][-1]:
            numarray[i][-1] = numarray[i][-1][:-1]
        if shouldprint:
            print(numarray[i])
    return numarray


def answer():
    pyramid = parseNum("Problem 67.txt", True)
    print("")
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(len(pyramid[i])):
            pyramid[i][j] = int(pyramid[i][j])
            pyramid[i][j] += max(int(pyramid[i + 1][j]), int(pyramid[i + 1][j + 1]))
        pyramid.remove(pyramid[i + 1])
    print(pyramid)
answer()