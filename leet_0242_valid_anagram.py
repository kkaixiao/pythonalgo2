"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict_s = dict()
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            dict_s[char] = dict_s.get(char, 0) - 1

        for k, v in dict_s.items():
            if v > 0:
                return False

        return True


    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        dict_s = dict()
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1

        for char in t:
            if char in dict_s:
                dict_s[char] -= 1
            else:
                return False

        for v in dict_s.values():
            if v != 0:
                return False

        return True

mysol = Solution()
print(mysol.isAnagram('a','ab'))