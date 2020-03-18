"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 2^0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16
Example 3:

Input: 218
Output: false
"""

class Solution:
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        elif n == 2 or n == 1:
            return True
        if n % 2 != 0 and n != 1:
            return False
        else:
            return self.isPowerOfTwo(n//2)

sol = Solution()

print(sol.isPowerOfTwo(9))