"""
Given a positive integer num, write a function which returns True if num is a perfect square
else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution:


    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        start, end = 1, num

        while start <= end:
            mid = end + (start - end) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                start = mid + 1
            else:
                end = mid - 1

        return False

    # a cheating method LOL
    def isPerfectSquare3(self, num: int) -> bool:
        t = num ** 0.5
        return (t//1) == t

    # time exceed
    def isPerfectSquare2(self, num: int) -> bool:
        if num == 1:
            return True
        for i in range(num//2+1):
            if i**2 == num:
                return True
        return False

obj = Solution()
print(obj.isPerfectSquare3(256))
