def parsefile(filename):
    file = open(filename)
    array = file.readlines()
    return array

print(parsefile("Problem Text Files/Problem 54.txt"))