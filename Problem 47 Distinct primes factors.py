def is_prime(num):
    for i in range(3, int(num**.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def calc_prime_array(max):
    prime_array = [2]
    for i in range(3, max + 1, 2):
        if is_prime(i):
            prime_array.append(i)
    return prime_array


def calc_prime_factors(num, primes):
    prime_factors = []
    current = num
    while current != 1:
        for i in range(0, current):
            if current % primes[i] == 0:
                prime_factors.append(primes[i])
                current = int(current / primes[i])
                break
    return prime_factors


def answer():
    consecutive = 0
    consecutive_numbers = []
    prime_array = calc_prime_array(1000000)
    i = 3
    while consecutive != 4:
        if len(set(calc_prime_factors(i, prime_array))) == 4:
            consecutive += 1
            consecutive_numbers.append(i)
        else:
            consecutive = 0
            consecutive_numbers = []
        i += 1
        print(i)
    print(consecutive_numbers)
answer()