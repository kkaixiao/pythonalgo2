"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially
a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one
by one to see if T has its subsequence. In this scenario, how would you change your code?
"""

class Solution:
    # quite slow version
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = -1
        for char in s:
            found = False
            while idx < len(t)-1:
                idx += 1
                if char == t[idx]:
                    found = True
                    break
            if not found:
                return False
        return True

    # fairly fast version
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                t = t[t.index(char)+1:]
            else:
                return False

        return True

    # two pointers approach, but not efficient
    def isSubsequence(self, s: str, t: str) -> bool:
        start, end = 0, 0
        while start < len(s) and end < len(t):
            while end < len(t) and s[start] != t[end]:
                end += 1
            if end < len(t) and s[start] == t[end]:
                start += 1
                end += 1
        return start == len(s)