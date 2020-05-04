"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if -7 < num < 7:
            return str(num)
        digits = []
        res = ''
        if num < 0:
            res = '-'
        num = abs(num)
        while num > 6 or num < -6:
            digits.append(num % 7)
            num //= 7
        digits.append(num)

        for i in range(len(digits) - 1, -1, -1):
            res += str(digits[i])

        return res

    # direct string operation without using list
    def convertToBase7(self, num: int) -> str:
        if -7 < num < 7:
            return str(num)

        positive = True
        if num < 0:
            positive = False
        res = ''
        num = abs(num)
        while num > 6 or num < -6:
            res = str(num % 7) + res
            num //= 7

        res = str(num) + res
        if not positive:
            res = '-' + res
        return res