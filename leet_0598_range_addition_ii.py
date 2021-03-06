"""
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with
two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a
and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all
the operations.

Example 1:
Input:
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation:
Initially, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
"""


class Solution:
    # first version failed, time exceeded
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        mat = []
        for i in range(n):
            mat.append([0] * m)

        for r in range(m):
            for c in range(n):
                for op in ops:
                    if r < op[0] and c < op[1]:
                        mat[r][c] += 1
        res = []
        for r in range(m):
            for c in range(n):
                res.append(mat[r][c])

        return res.count(max(res))

    # 2nd solution, much conciser, however speed is not optimal
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])

        return m*n