"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, s):
        num = 0
        for i in range(len(s)):
            num += (ord(s[i])-64) * (26 ** (len(s)-i-1))
        return num



s1 = 'BAA'

sol = Solution()

print(sol.titleToNumber(s1))