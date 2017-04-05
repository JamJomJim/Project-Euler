import math
def answer():
    facttotal = 0
    for i in range(3,1000000):
        num = i
        total = 0
        for digit in range(len(str(num))):
            total += math.factorial(int(str(num)[digit]))
        if num == total:
            print(total)
            facttotal += num
    print(facttotal)
answer()