"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those
numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


class Solution:
    def isHappy(self, n):
        global his
        his = []
        temp = 0

        for i in str(n):
            temp += int(i) ** 2

        if temp == 1:
            return True
        else:
            if temp in his:
                return False
            else:
                his.append(temp)
                return self.isHappy(temp)

mysol = Solution()
print(mysol.isHappy(13))
# def isHappy(self, n):
#     ans = []
#     temp = n
#     while temp != 1:
#         temp = self.calculate(temp)
#         if temp in ans:
#             return False
#         else:
#             ans.append(temp)
#
#     return True
#
#
# def calculate(self, n):
#     str_n = str(n)
#     temp = 0
#
#     for i in str_n:
#         temp += int(i) ** 2
#
#     return temp
