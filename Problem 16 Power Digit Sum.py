def answer():
    number = 2**1000
    sum = 0
    for i in range(0,len(str(number))):
        sum += int(str(number)[i])
    print(sum)
answer()