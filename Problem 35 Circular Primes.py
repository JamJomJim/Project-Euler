def is_prime(num):
    if not 2 and num % 2 == 0:
        return False
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


def rotate_array(array):
    array = array[1:] + array[0:1]
    return array


def all_prime(array):
    for number in array:
        if not is_prime(number):
            return False
    return True


def answer():
    prime_array = calc_prime_array(1000000)
    count = 0
    for prime in prime_array:
        rotations = [prime]
        array = num_to_digit_array(rotations[0])
        for i in range(0, len(array) - 1):
            array = rotate_array(array)
            rotations.append(digit_array_to_num(array))
        if all_prime(rotations):
            print(rotations)
            count += 1
    print(count)

answer()
