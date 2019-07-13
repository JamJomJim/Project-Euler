def answer():
    highest_solutions = 0
    best_p = 1
    for p in range(1, 1001):
        print(p)
        solutions = 0
        for a in range(1, p):
            for b in range(a, p):
                if p - a - b < 0:
                    break
                if float(p - a - b) == (a ** 2 + b ** 2) ** (1/2):
                    solutions += 1
        if solutions > highest_solutions:
            highest_solutions = solutions
            best_p = p

    print(best_p)


answer()
