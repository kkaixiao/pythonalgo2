"""


"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 0
        res = 0
        for e in set(s):
            num = s.count(e)
            if num % 2 == 0:
                res += num
            else:
                res = res + num - 1
                odd = 1
        return res + odd