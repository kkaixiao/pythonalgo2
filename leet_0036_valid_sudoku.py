""""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsDict = [set() for i in range(9)]
        colsDict = [set() for i in range(9)]
        subSqDict = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                currVal = board[r][c]

                SubSqKey = (r // 3 * 3 + c // 3)

                if currVal in rowsDict[r] or currVal in colsDict[c] or currVal in subSqDict[SubSqKey]:
                    return False

                rowsDict[r].add(currVal)
                colsDict[c].add(currVal)
                subSqDict[SubSqKey].add(currVal)

        return True