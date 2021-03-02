"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in
spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pos = (0, 0)
        move = 0
        i = 1
        target = n ** 2
        while i <= target:
            if pos[0] >= 0 and pos[0] < len(mat) and pos[1] >= 0 and pos[1] < len(mat[0]) \
                    and mat[pos[0]][pos[1]] == 0:

                mat[pos[0]][pos[1]] = i
                i += 1
            else:
                pos = (pos[0] - moves[move][0], pos[1] - moves[move][1])

                move = (move + 1) % 4

            pos = (pos[0] + moves[move][0], pos[1] + moves[move][1])

        return mat