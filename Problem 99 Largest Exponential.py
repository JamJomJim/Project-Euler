import math
def parseNum(filename, shouldprint):
    numbergrid = open(filename)
    read = False
    numarray = []
    while not read:
        curline = numbergrid.readline()
        if curline == "":
            break
        numarray.append(curline.split(','))
    for i in range(len(numarray)):
        if "\n" in numarray[i][-1]:
            numarray[i][-1] = numarray[i][-1][:-1]
        if shouldprint:
            print(numarray[i])
    return numarray


def answer():
    pairs = list(parseNum('Problem 99.txt', False))
    largestexpline = 0
    for i in range(len(pairs)):
        if float(pairs[i][1]) * math.log(float(pairs[i][0])) >= float(pairs[largestexpline][1]) * math.log(float(pairs[largestexpline][0])):
            print(i)
            print(pairs[i])
            largestexpline = i
    print(largestexpline)


answer()