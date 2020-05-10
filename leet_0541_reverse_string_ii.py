"""
Given a string and an integer k, you need to reverse the first k characters for every 2k
characters counting from the start of the string. If there are less than k characters left,
reverse all of them. If there are less than 2k but greater than or equal to k characters, then
reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        count=-1
        for i in range(0, len(s), k):
            count += 1
            if count%2 == 0:
                res += s[i:i+k][::-1]
            else:
                res += s[i:i+k]
        return res

    # use my own reverse processing
    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        count=-1
        for i in range(0, len(s), k):
            count += 1
            if count%2 == 0:
                temp = ''
                for j in range(len(s[i:i+k])-1, -1, -1):
                    temp = temp + s[i:i+k][j]
                res += temp

            else:
                res += s[i:i+k]
        return res