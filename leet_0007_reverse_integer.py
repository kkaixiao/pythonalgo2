"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume
that your function returns 0 when the reversed integer overflows.
"""


def reverse_integer(num):
    if num > (2 ** 31 - 1) or num < -(2 ** 31):
        return 0
    if 10 > num > 0 or -10 < num < 0:
        return num
    digits = []
    abs_num = abs(num)

    while abs_num > 0:
        digits.append(abs_num % 10)
        abs_num //= 10

    res = 0
    for i in range(len(digits)):
        res += digits[i] * 10 ** (len(digits) - i - 1)

    if num < 0:
        res = 0 - res

    return 0 if (res > (2 ** 31 - 1) or res < -(2 ** 31)) else res


from math import floor, log10
def reverse_integer2(num):

    if num > (2 ** 31 - 1) or num < -(2 ** 31):
        return 0
    if 10 > num >= 0 or -10 < num < 0:
        return num

    abs_num = abs(num)

    num_len = len(str(abs_num))  #this is a traditional way to find a length of a number

    # num_len = floor(log10(abs_num) + 1)  # this is by using math.log10() function
    res = 0
    count = 1
    while abs_num > 0:
        res += abs_num % 10 * (10 ** (num_len - count))
        abs_num //= 10
        count += 1

    if num < 0:
        res = 0 - res

    return 0 if (res > (2 ** 31 - 1) or res < -(2 ** 31)) else res

print(reverse_integer2(301))