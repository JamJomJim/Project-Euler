def isfactor(num, factor):
    if num % factor == 0:
        return True
    else:
        return False


def checkforfactors(num):
    factors = 0
    for i in range(1, int(num**.5) + 1):
        if isfactor(num, i):
            #print(i)
            #print(num/i)
            factors += 2
    return factors


def gettriangle(tri):
    num = tri
    total = 0
    while num > 0:
        total += num
        num -= 1
    return total


def answer():
    found = False
    tri = 1
    while not found:
        if checkforfactors(gettriangle(tri)) > 500:
            found = True
            print(str(tri) + "th triangular number")
            print(gettriangle(tri))
        #print(str(tri) + "th triangular number has " + str(checkforfactors(gettriangle(tri))) + " factors")
        #print(gettriangle(tri))
        tri += 1

print(checkforfactors(28))
print(gettriangle(7))
answer()