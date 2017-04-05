def num_to_digit_array(num):
    array = []
    for digit in range(len(str(num))):
        array.append(int(str(num)[digit]))
    return array


def digit_array_to_num(array):
    num = ''
    for digit in range(len(array)):
        num += str(array[digit])
    return int(num)


# doesn't work for even numbers
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
    prime_array = calc_prime_array(1000000)
    prime_set = set(prime_array)
    truncated_primes = prime_array[4:]
    for prime in prime_array[4:]:
        for i in range(len(str(prime))):
            if int(str(prime)[i:]) not in prime_set:
                truncated_primes.remove(prime)
                break
            else:
                if int(str(prime)[:i + 1]) not in prime_set:
                    truncated_primes.remove(prime)
                    break
    print(truncated_primes)
    print(sum(truncated_primes))
answer()
