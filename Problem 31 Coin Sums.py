

def answer():
    coin_sum = 0
    possible_combinations = 1
    for pound in range(0, 3):
        coin_sum += 100

        for fifty in range(0, 5):

            for twenty in range(0, 11):

                for ten in range(0, 21):

                    for five in range(0, 41):

                        for two in range(0, 101):

                            if pound * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + two * 2 <= 200:
                                possible_combinations += 1

    print(possible_combinations)


answer()
