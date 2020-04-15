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

    def addStrings(self, num1: str, num2: str) -> str:
        return str((self.strToInteger(num1) + self.strToInteger(num2)))

    # faster solution using dictionary
    def strToInteger(self, s: str):
        mapDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        res = 0

        for i in range(len(s)):
            res *= 10
            res += mapDict[s[i]]

        return res

    # very slow solution using dictionary
    def strToInteger_slow(self, s: str):
        mapDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        lStr = len(s)
        res = 0
        for i in range(lStr):
            res += mapDict[s[i]] * (10 ** (lStr - i - 1))
        return res


    # fastest solution with map and bit operation
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(map(int, num1[::-1])), list(map(int, num2[::-1]))

        if len(num1)<len(num2):
            num1, num2 = num2, num1

        carry = 0
        for i in range(len(num1)):
            n = num2[i] if i<len(num2) else 0
            tmp = n + carry + num1[i]
            num1[i] = tmp%10
            carry = tmp//10

        if carry:
            num1.append(1)

        return ''.join(map(str, num1))[::-1]