def answer():
    string = ""
    for i in range(1, 1000000):
        string += str(i)
    total = 1
    for j in range(0,7):
        total *= int(string[(10**j) - 1])
    print(total)


answer()