def parsefile(filename):
    file = open(filename)
    curline = file.readline().replace('"', "")
    array = curline.split(',')
    return array


def answer():
    textarray = sorted(parsefile("Problem Text Files/Problem 22.txt"))
    totalsum = 0

    for name in textarray:
        namecharsum = 0
        for char in name.lower():
            namecharsum += ord(char) - 96
        totalsum += namecharsum * (textarray.index(name) + 1)

    print(totalsum)


answer()
