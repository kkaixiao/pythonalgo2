"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same
backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore
 it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

def palindrome(num):
    if num < 0:
        return False
    if num < 10:
        return True
    half_len = len(str(num))//2
    len_mod = len(str(num)) % 2
    return str(num)[:half_len] == reverse_chars(str(num)[half_len+len_mod:])


def reverse_chars(chars):
    res = ''
    for i in range(len(chars)):
        res += chars[-i-1]
    return res


def palindrome1(num):
    if num < 0:
        return False
    if num < 10:
        return True
    half_len = len(str(num))//2
    len_mod = len(str(num)) % 2
    return str(num)[:half_len] == reverse_chars(str(num)[half_len+len_mod:])


def palindrome_direct_int(num):
    if 0 <= num <= 9:
        return True
    if num < 0 or not(num % 10):
        return False
    return num == reverse_int(num)


def reverse_int(num):
    reverse = 0
    while num > 0:
        rem = num % 10
        reverse = reverse * 10 + rem
        num = int(num / 10)
    return reverse


def palindrome_num_array(num):
    if 0 <= num <= 9:
        return True
    if num < 0 or not(num % 10):
        return False
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10

    for i in range(len(digits)//2):
        if digits[i] != digits[-i-1]:
            return False

    return True


def palindrome_num_dict(num):
    if 0 <= num <= 9:
        return True
    if num < 0 or not(num % 10):
        return False
    digits = {}
    count = 0
    while num > 0:
        digits[count] = num % 10
        num = num // 10
        count += 1

    for i in range(count//2):
        if digits[i] != digits[count-i-1]:
            return False

    return True


import math


def palindrome_num_direct2(num):

    if 0 <= num <= 9:
        return True
    if num < 0 or num % 10 == 0:
        return False

    digit_num = int(math.log10(num)) + 1

    for i in range(digit_num//2):
        if num//(10**(digit_num-i-1)) % 10 != num//(10**i) % 10:
            return False

    return True


def palindrome_num_direct3(num, digit):

    if 0 <= num <= 9:
        return True
    if num < 0 or num % 10 == 0:
        return False

    digit_num = int(math.log10(num)) + 1

    # to add recursion version

    # for i in range(digit_num//2):
    #     if num//(10**(digit_num-i-1)) % 10 != num//(10**i) % 10:
    #         return False


    return True

print(palindrome_num_direct3(10701))

