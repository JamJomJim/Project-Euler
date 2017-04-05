import itertools
def answer(number):
    options = list(itertools.product('rl', repeat=number*2))
    print(len(options))
    for arb in range(0,10):
        for option in options:
            rcount = 0
            lcount = 0
            for i in range(0, number*2):
                if option[i] == 'r':
                    rcount += 1
                else:
                    if option[i] == 'l':
                        lcount += 1
            if rcount > number or lcount > number:
                options.remove(option)

    print(len(options))
# for i in range(1,8):
#         answer(i)
print(len(list(itertools.permutations('rrrrllll', 4))))