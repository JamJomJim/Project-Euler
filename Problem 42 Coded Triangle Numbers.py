import string


def parseNum(filename):
    file = open(filename)
    curline = file.readline().replace('"', "")
    array = curline.split(',')
    return array


def create_triangular_list(limit):
    triangular_list = []
    for i in range(1, limit + 1):
        triangular_list.append(i*(i+1)/2)
    return triangular_list


letter_to_int = dict()
for index, letter in enumerate(string.ascii_uppercase, 1):
    letter_to_int[letter] = index
words = parseNum("Problem 42.txt")
amount = 0
tri_set = set(create_triangular_list(1000))
for word in words:
    word_num = 0
    for letter in word:
        word_num += letter_to_int[letter]
    if word_num in tri_set:
        amount += 1

print(amount)



