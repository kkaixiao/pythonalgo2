"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order
of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            try:
                s_dict[i] = s[i+1:].index(s[i]) + i + 1

            except ValueError:
                s_dict[i] = -1
            try:
                t_dict[i] = t[i+1:].index(t[i]) + i + 1
            except ValueError:
                t_dict[i] = -1

        for k,_ in s_dict.items():
            if s_dict[k] != t_dict[k]:
                return False
        return True


    def isIsomorphic2(self, s, t):
        s_dict = dict()
        t_dict = dict()

        for i in range(len(s)):

            s_dict[s[i]] = s_dict.get(s[i], '') + str(i)
            t_dict[t[i]] = t_dict.get(t[i], '') + str(i)

        for item in zip(s_dict.values(), t_dict.values()):
            if item[0] != item[1]:
                return False


        return True


    def isIsomorphic3(self, s, t):
        d = {}
        for i, j in zip(s, t):
            if i in d:
                if d[i] != j:
                    return False
            elif j not in d.values():
                d[i] = j
            else:
                return False
        return True

s1 = "paper"
t1 = "title"

mysolution = Solution()
print(mysolution.isIsomorphic2(s1, t1))