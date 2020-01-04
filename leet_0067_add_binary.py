"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


def add_binary(chars1, chars2):
    if len(chars1) > len(chars2):
        list1, list2 = list(chars1), list(chars2)
    else:
        list1, list2 = list(chars2), list(chars1)
    is_carry = 0
    res = []
    for idx2 in range(len(list2)-1, -1, -1):
        idx1 = idx2 + len(list1) - len(list2)
        sum_bits_and_is_carry = int(list1[idx1]) + int(list2[idx2]) + is_carry
        res.insert(0, sum_bits_and_is_carry % 2)
        is_carry = sum_bits_and_is_carry // 2

    for i in range(len(list1) - len(list2)-1, -1, -1):

        sum_bits_and_is_carry = int(list1[i]) + is_carry
        res.insert(0, sum_bits_and_is_carry % 2)
        is_carry = sum_bits_and_is_carry // 2

    if is_carry == 1:
        res.insert(0, is_carry)

    res_str = [None]*len(res)
    for i in range(len(res)):
        res_str[i] = str(res[i])

    return ''.join(res_str)




print(add_binary('11', '1'))