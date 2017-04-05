def divisors(num):
    divs = []
    for i in range(1, int(num**.5) + 1):
        if num % i == 0:
            divs.append(i)
            pair = int(num/i)
            if i != pair and pair != num:
                divs.append(pair)
    return divs


def divsum(num):
    total = 0
    for div in divisors(num):
        total += div
    return total


def isabundant(num):
    if divsum(num) > num:
        return True
    else:
        return False


def answer():
    abundnums = []
    for i in range(2, 28123):
        if isabundant(i):
            abundnums.append(i)
    abund_set = set(abundnums)
    print(abundnums)
    total = 276
    for num in range(24, 28123):
        hassum = False
        i = 0
        while abundnums[i] <= num:
            need = num - abundnums[i]
            if need in abund_set:
                hassum = True
                break
            i += 1
        if not hassum:
            total += num
    print(total)


answer()
