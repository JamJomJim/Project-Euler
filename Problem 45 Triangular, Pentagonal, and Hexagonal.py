def create_triangular_list(limit):
    triangular_list = []
    for i in range(1, limit + 1):
        triangular_list.append(i*(i+1)/2)
    return triangular_list


def create_pentagonal_list(limit):
    pentagonal_list = []
    for i in range(1, limit + 1):
        pentagonal_list.append(i * (3*i - 1)/2)
    return pentagonal_list


def create_hexagonal_list(limit):
    hexagonal_list = []
    for i in range(1, limit + 1):
        hexagonal_list.append(i*(i*2 - 1))
    return hexagonal_list


def answer(limit):
    hex_list = create_hexagonal_list(limit)
    pent_list = create_pentagonal_list(limit)
    tri_list = create_triangular_list(limit)
    hex_set = set(hex_list)
    pent_set = set(pent_list)
    for tri in tri_list:
        if tri in hex_set and tri in pent_set:
            print(tri)
    print("done")


answer(100000)
