def parseNum(filename, shouldprint):
    numbergrid = open(filename)
    read = False
    numarray = []
    while not read:
        curline = numbergrid.readline()
        if curline == "":
            break
        numarray.append(curline.split(' '))
    if shouldprint:
        for i in range(len(numarray)):
            if "\n" in numarray[i][-1]:
                numarray[i][-1] = numarray[i][-1][0:2]
            print(numarray[i])
    return numarray


def answer():
    numarray = parseNum("Number Grid.txt", False)
    maxprod = 0
    for y in range(len(numarray)):
        for x in range(len(numarray[y])):
            product = 1
            if y - 3 >= 0:
                for mult in range(0, 4):
                    product *= int(numarray[y - mult][x])
                if product > maxprod:
                    maxprod = product
            product = 1
            if x - 3 >= 0:
                for mult in range(0, 4):
                    product *= int(numarray[y][x - mult])
                if product > maxprod:
                    maxprod = product
            product = 1 
            if y - 3 >= 0 and x - 3 >= 0:
                for mult in range(0, 4):
                    product *= int(numarray[y - mult][x - mult])
                    if product > maxprod:
                        maxprod = product
            product = 1
            if y - 3 >= 0 and x + 3 <= 19:
                for mult in range(0, 4):
                    product *= int(numarray[y - mult][x + mult])
                    if product > maxprod:
                        maxprod = product
    print(maxprod)


answer()