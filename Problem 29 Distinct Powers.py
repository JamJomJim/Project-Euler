def answer():
    powers = []
    for a in range(2, 6):
        for b in range(2, 6):
            powers.append(a**b)
    powers = sorted(powers)
    i= 0
    while i <= (len(powers) - 2):
        if powers[i] == powers[i + 1]:
            powers.remove(powers[i])
            i -= 1
        i += 1
    print(len(powers))

answer()
