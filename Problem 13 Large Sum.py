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
    numarray = parseNum("Problem 13.txt", False)
    total = 0
    for num in numarray:
        print(num)
        total += int(num[0])
    print(str(total)[0:10])


answer()