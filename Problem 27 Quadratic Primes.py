def is_prime(num):
    if not 2 and num % 2 == 0:
        return False
    for i in range(3, int(num**.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def answer():
    best_a = 0
    best_b = 0
    best_n = 0
    for a in range(-1000, 1000):
        for b in range(1, 1000):
            number = b
            n = 0
            while number >= 2 and is_prime(number):
                n += 1
                if n > best_n:
                    best_a = a
                    best_b = b
                    best_n = n
                number = n*n + n*a + b
    print("A = " + str(best_a))
    print("B = " + str(best_b))
    print("N = " + str(best_n))
    print(str(best_a * best_b))

answer()

