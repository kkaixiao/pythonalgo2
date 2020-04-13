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

    # a faster approach
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for e in set(s):
            res += (s.count(e)//2)*2
        if res < len(s):
            return res + 1
        else:
            return res