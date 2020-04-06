"""
Given a string, find the first non-repeating character in it and return it's index. If it
doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    # first dictionary approach
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char, 0) + 1
        for k, v in charDict.items():
            if v == 1:
                return s.index(k)
        return -1

    # second dictionary approach
    def firstUniqChar(self, s: str) -> int:
        charDict = {}
        for char in s:
            charDict[char] = charDict.get(char, 0) + 1
        for i, char in enumerate(s):
            if charDict[char] == 1:
                return i
        return -1

    # set count approach
    def firstUniqChar(self, s: str) -> int:
        lst = []

        for char in set(s):
            if s.count(char) == 1:
                lst.append(s.index(char))

        if lst != []:
            return min(lst)

        return -1