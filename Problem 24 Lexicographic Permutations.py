import itertools
def answer():
    perms = list(itertools.permutations('0123456789', 10))
    print(perms[999999])

answer()