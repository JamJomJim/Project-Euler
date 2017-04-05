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
    divsum = 0
    for div in divisors(num):
        divsum += div
    return divsum


def isamicable(num):
    if num == divsum(divsum(num)) and num != divsum(num):
        return True
    else:
        return False


def answer():
    total = 0
    for i in range(2, 10000):
        if isamicable(i):
            total += i
    print(total)

answer()