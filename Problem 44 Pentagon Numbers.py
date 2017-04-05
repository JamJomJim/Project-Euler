def create_pentagon_array(amount):
    array = []
    for i in range(1, amount + 1):
        array.append(i * (3*i - 1)/2)
    return array


def answer(limit):
    pent_array = create_pentagon_array(limit)
    pent_set = set(pent_array)
    lowest_diff = 100000000
    for i in range(limit - 2):
        for j in range(i + 1, limit - 1):
            pent_sum = pent_array[j] + pent_array[i]
            pent_diff = pent_array[j] - pent_array[i]
            if pent_sum in pent_set and pent_diff in pent_set and pent_diff < lowest_diff:
                lowest_diff = pent_diff
                print(str(pent_array[j]) + "and" + str(pent_array[i]))
    print(lowest_diff)


answer(10000)
