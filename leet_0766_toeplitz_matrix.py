"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at
most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r, c = len(matrix), len(matrix[0])

        for x in range(r):
            if not self.isDiagSame(matrix, x, 0, r, c):
                return False
        for y in range(1, c):
            if not self.isDiagSame(matrix, 0, y, r, c):
                return False
        return True

    def isDiagSame(self, matrix, firstR, firstC, r, c):
        nextR, nextC = firstR, firstC
        while nextR < r - 1 and nextC < c - 1:
            nextR += 1
            nextC += 1
            if matrix[nextR][nextC] != matrix[firstR][firstC]:
                return False
        return True