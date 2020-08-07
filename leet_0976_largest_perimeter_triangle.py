"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


class Solution:
    # over time
    def largestPerimeter(self, A: List[int]) -> int:
        C = itertools.combinations(A, 3)
        maxPerimeter = 0
        for c in C:
            c = sorted(c)
            if c[0] + c[1] > c[2] and sum(c) > maxPerimeter:
                maxPerimeter = sum(c)
        return maxPerimeter

    # much faster
    def largestPerimeter(self, A):
        A.sort()

        for i in range(len(A)-1, 1, -1):
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2]

        return 0
