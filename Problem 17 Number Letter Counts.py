nums = {
    0: '',
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'onethousand'
}

def answer():
    total = 0
    for i in range(1, 1001):
        num_string = ""
        ones_digit = i % 10
        tens_digit = (i % 100 - ones_digit) / 10
        hundreds_digit = (i % 1000 - tens_digit * 10 - ones_digit) / 100
        if nums.__contains__(i):
            num_string = nums[i]
            #print(nums[i])
        else:
            if hundreds_digit > 0:
                if nums.__contains__(tens_digit*10 + ones_digit):
                    num_string = nums[hundreds_digit] + "hundredand" + nums[tens_digit*10 + ones_digit]
                else:
                    num_string = nums[hundreds_digit] + "hundredand" + nums[tens_digit * 10] + nums[ones_digit]
                #print(num_string)
            else:

                num_string = nums[tens_digit * 10] + nums[ones_digit]
                #print(num_string)
        if num_string[-3:] == "and":
            num_string = num_string[:-3]
        print(num_string)
        total += len(num_string)
    print(total + 6)
answer()