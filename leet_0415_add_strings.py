"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1
and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    # very slow solution using dictionary
    def addStrings(self, num1: str, num2: str) -> str:
        return str((self.strToInteger(num1) + self.strToInteger(num2)))

    def strToInteger(self, s: str):
        mapDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        lStr = len(s)
        res = 0
        for i in range(lStr):
            res += mapDict[s[i]] * (10 ** (lStr - i - 1))
        return res