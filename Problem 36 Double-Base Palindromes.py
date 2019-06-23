def isPalindrome(num):

    for i in range(0, int(len(str(num)) / 2)):
        if str(num)[i] != str(num)[-1 - i]:
            return False
    return True


def answer():
    palSum = 0
    for i in range(0, 1000000):
        if isPalindrome("{0:b}".format(i)) and isPalindrome(i):
            palSum += i
    print(palSum)


answer()
