

"""
Find the sum of digits of a positive integer number using recursion
"""


# 10.    10  / 10  =  1,  rem 0
# 11.    11  / 10  =  1,  rem 1
# 112.   112 / 10  =  11, rem 2
#                  =  11 / 10 = 1,  rem 1
#                         2   +   1    +    1


def sumOfDigits(number):
    assert number >= 0 and int(number) == number, 'Number must be a positive integer number'
    if number < 10:
        return number
    return int(number) % 10 + sumOfDigits(int(number//10))


print(sumOfDigits(11112))