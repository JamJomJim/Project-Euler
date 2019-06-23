pandigital_products = []
pandigital_sum = 0

def isPandigital(a, b):
    c = a * b
    requireddigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    combinationdigits = []

    combined = str(a) + str(b) + str(c)
    if len(combined) == 9:
        for digit in str(combined):
            combinationdigits.append(digit)
        combinationdigits.sort()
        if combinationdigits == requireddigits:
            pandigital_products.append(c)


for i in range(0, 2000):
    for j in range(0, 100):
        isPandigital(i, j)
    print(i)

# removes duplicates in list
pandigital_products = list(dict.fromkeys(pandigital_products))

for number in pandigital_products:
    pandigital_sum += number

print(pandigital_sum)
