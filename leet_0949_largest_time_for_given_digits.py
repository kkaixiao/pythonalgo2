"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is
larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
"""

from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        perms = permutations(A)
        validTime = []
        for perm in list(perms):
            hours = perm[0]*10 + perm[1]
            minutes = perm[2]*10 + perm[3]
            if (0<=hours <= 23) and (0<=minutes<=59):
                validTime.append(perm[0]*1000+perm[1]*100+perm[2]*10+perm[3])
        if len(validTime) == 0:
            return ''
        maxTime = max(validTime)
        maxTimeStr = format(maxTime, '04d')
        res = maxTimeStr[:2] + ':' + maxTimeStr[2:]
        return res