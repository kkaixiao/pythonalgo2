"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]




Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        maxNum = max(A)
        if A.count(maxNum) > 1:
            return False

        iMax = A.index(maxNum)

        if iMax == 0 or iMax == (len(A) - 1):
            return False

        tempL = tempR = A[iMax]

        for i in range(iMax - 1, -1, -1):
            if tempL <= A[i]:
                return False
            tempL = A[i]

        for j in range(iMax + 1, len(A)):
            if tempR <= A[j]:
                return False
            tempR = A[j]

        return True