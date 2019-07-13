import itertools

def is_pandigital(num):
    digits = []
    for j in range(1, len(str(num)) + 1):
        digits.append(j)
    for letter in str(num):
        if int(letter) in digits:
            digits.remove(int(letter))
        else:
            return False
    if len(digits) == 0:
        return True
    else:
        return False


def is_prime(num):
    if num != 2 and num % 2 == 0:
        return False
    for i in range(3, int(num**.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def answer():
    all_perms = list(itertools.permutations([7, 6, 5, 4, 3, 2, 1]))
    for perm in all_perms:
        num = int(''.join(map(str, perm)))
        if is_prime(num):
            print(num)


answer()
