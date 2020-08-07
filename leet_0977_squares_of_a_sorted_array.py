"""
iven an array of integers A sorted in non-decreasing order, return an array of the squares of
each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        f = lambda x: x*x
        A = [f(z) for z in A ]
        return sorted(A)

    # two pointer
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort()
        start, end, endPointer = 0, len(A) - 1, len(A) - 1
        res = [None] * len(A)

        while end >= start:
            leftSquare = A[start] * A[start]
            rightSquare = A[end] * A[end]

            if rightSquare > leftSquare:
                res[endPointer] = rightSquare
                endPointer -= 1
                end -= 1

            else:
                res[endPointer] = leftSquare
                endPointer -= 1
                start += 1

        return res