def answer():
    highestSolutions = 0
    bestP = 1
    for p in range(1, 1001):
        print(p)
        solutions = 0
        for a in range(1, p):
            for b in range(a, p):
                if p - a - b < 0:
                    break
                if float(p - a - b) == (a ** 2 + b ** 2) ** (1/2):
                    solutions += 1
        if solutions > highestSolutions:
            highestSolutions = solutions
            bestP = p

    print(bestP)

answer()
