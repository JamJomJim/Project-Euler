def isfifth(num):
    total = 0
    for i in range(len(str(num))):
        total += int(str(num)[i])**5
    return total


def answer():
    fifths = []
    for i in range(2, 1000000):
        if i == isfifth(i):
            fifths.append(i)
    print(fifths)
    total = 0
    for fifth in fifths:
        total += fifth
    print(total)
answer()
