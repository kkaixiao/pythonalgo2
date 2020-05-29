"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a
smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of
all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as
many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rowNum, colNum = len(M), len(M[0])

        res = [[None] * colNum for i in range(rowNum)]

        for r in range(rowNum):

            startRowIdx, endRowIdx, rowDiv = r - 1, r + 1, 3
            rowDiv = 3
            if r == 0:
                startRowIdx, endRowIdx, rowDiv = 0, 1, 2
            elif r == rowNum - 1:
                startRowIdx, endRowIdx, rowDiv = r - 1, r, 2

            for c in range(colNum):
                startColIdx, endColIdx, colDiv = c - 1, c + 1, 3
                if c == 0:
                    startColIdx, endColIdx, colDiv = 0, 1, 2
                elif c == colNum - 1:
                    startColIdx, endColIdx, colDiv = c - 1, c, 2

                sumCells = 0

                if rowNum == 1:
                    endRowIdx, rowDiv = 0, 1

                if colNum == 1:
                    endColIdx, colDiv = 0, 1

                for rowIdx in range(startRowIdx, endRowIdx + 1):
                    for colIdx in range(startColIdx, endColIdx + 1):
                        sumCells += M[rowIdx][colIdx]

                res[r][c] = int(sumCells / (rowDiv * colDiv))

        return res