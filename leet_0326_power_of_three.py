"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n % 3 != 0:
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(n // 3)


    def isPowerOfThree_ite(self, n: int) -> bool:
        while n > 1:
            n = n/3
        return n == 1


    def isPowerOfThree_O1(self, n: int) -> bool:
        if n < 1:
            return False

        res = math.log10(n) / math.log10(3)

        return math.floor(res) == math.ceil(res)