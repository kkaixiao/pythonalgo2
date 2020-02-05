"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a
non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may
be separated by a single space.
"""

class Solution:
    def wordPattern(self, pattern, str):

        pat = dict()
        for i in range(len(pattern)):
            if pattern[i] not in pat:
                pat[pattern[i]] = [i]
            else:
                pat[pattern[i]].append(i)

        list1 = list(str.split(' '))
        if len(list1) != len(pattern):
            return False

        st = dict()
        for j in range(len(list1)):
            if list1[j] not in st:
                st[list1[j]] = [j]
            else:
                st[list1[j]].append(j)

        val_st = list(st.values())
        val_pat = list(pat.values())
        return val_st == val_pat