"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row,
column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is
contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def isMagicSquare(lst):
            for i in lst:
                if i < 1 or i > 9:
                    return False
            if lst[0] == lst[1]:
                return False
            if lst[4] != 5:
                return False

            if lst[8] - lst[4] != lst[4] - lst[0]:
                return False

            if lst[0] + lst[1] + lst[2] != lst[3] + lst[4] + lst[5]:
                return False
            if lst[0] + lst[3] + lst[6] != lst[1] + lst[4] + lst[7]:
                return False

            return True

        rows, cols, cnt = len(grid), len(grid[0]), 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                a = []
                for i in range(3):
                    for j in range(3):
                        a.append(grid[r + i][c + j])

                if isMagicSquare(a):
                    cnt += 1

        return cnt
