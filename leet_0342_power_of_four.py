
"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True

        if num == 0 or num % 4 != 0:
            return False

        return self.isPowerOfFour(num // 4)


    def isPowerOfFour_ite(self, num: int) -> bool:
            while num > 1:
                num /= 4
            return num == 1


    def isPowerOfFour_O1(self, num: int) -> bool:
        if num < 1:
            return False


        return math.floor(math.log10(num) / math.log10(4)) == math.ceil(math.log10(num) / math.log10(4))

