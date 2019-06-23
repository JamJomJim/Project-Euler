def answer():
    total = 1
    num = 1
    increment = 2
    while num < 1001**2:
        for i in range(1, 5):
            num += increment
            total += num
        increment += 2
    print(total)


answer()
