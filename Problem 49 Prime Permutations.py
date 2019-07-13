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


def answer():
    prime_array = calc_prime_array(10000)
    for i in range(0, len(prime_array)):
        for j in range(i + 1, len(prime_array)):
            k = prime_array[j] + (prime_array[j] - prime_array[i])
            if is_prime(k) and k < 10000:
                if sorted(list(str(prime_array[i]))) == sorted(list(str(prime_array[j]))) and sorted(list(str(prime_array[i]))) == sorted(list(str(k))):
                    print(prime_array[i])
                    print(prime_array[j])
                    print(k)
                    print(str(prime_array[i]) + str(prime_array[j]) + str(k))


answer()
