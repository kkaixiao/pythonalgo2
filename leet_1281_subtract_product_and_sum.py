"""
Given an integer number n, return the difference between the product of its digits and
the sum of its digits.


Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""
from math import log10, floor

def subtract_product_and_sum(num):
    product_num = 1
    sum_num = 0
    for digit in str(num):
        product_num *= int(digit)
        sum_num += int(digit)
    return product_num - sum_num


def subtract_product_and_sum2(num):
    product_num = 1
    sum_num = 0

    len_num = int(log10(num))
    for i in range(len_num+1):
        product_num *= num//(10**i)%10
        sum_num += num//(10**i)%10
    return product_num - sum_num





print(subtract_product_and_sum(4567801))