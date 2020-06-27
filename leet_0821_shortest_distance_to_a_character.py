"""
Given a string S and a character C, return an array of integers representing the shortest distance
from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [inf] * len(S)
        foundIdx = []
        for i in range(len(S)):
            if S[i] == C:
                res[i] = 0
                foundIdx.append(i)
        if len(foundIdx) == 0:
            return res

        disArr = [None] * len(foundIdx)
        for i in range(len(res)):
            for j in range(len(disArr)):
                disArr[j] = abs(foundIdx[j] - i)
            res[i] = min(disArr)
        return res
