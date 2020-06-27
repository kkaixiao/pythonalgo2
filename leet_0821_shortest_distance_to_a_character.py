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



class Solution:
    # a much faster solution with O(n)
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        S = ' '+S
        lMat = 0  # here lMat means: last match
        for i in range(len(S)):
            res.append(i-lMat)
            if S[i] == C:
                if lMat:
                    res[(i+lMat)//2 + (i+lMat)%2:] = res[(i + lMat)//2:lMat-1:-1]
                else:
                    res[0::1] = res[i::-1]
                lMat = i
        return res[1:]