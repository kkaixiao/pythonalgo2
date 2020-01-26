"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops,
and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase
characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east,
west, and south), then moves in that direction until it chooses to stop, reaches the edge of the
board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks
cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
In this example the rook is able to capture all the pawns.


Example 2:
Input: [[".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 0
Explanation:
Bishops are blocking the rook to capture any pawn.


Example 3:
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation:
The rook can capture the pawns at positions b5, d6 and f5.

Note:

1. board.length == board[i].length == 8
2. board[i][j] is either 'R', '.', 'B', or 'p'
3. There is exactly one cell with board[i][j] == 'R'

"""

class Solution:

    def rec_one_direction_count(self, board, row_id, col_id, direction):
        if(row_id<0 or col_id<0 or row_id>=8 or col_id>=8):
            return 0
        if(board[row_id][col_id] == '.' or board[row_id][col_id]=="R"):
            if(direction == 'up'):
                return self.rec_one_direction_count(board, row_id, col_id - 1, direction)
            elif(direction == 'down'):
                return self.rec_one_direction_count(board, row_id, col_id+1, direction)
            elif(direction == 'left'):
                return self.rec_one_direction_count(board, row_id-1, col_id, direction)
            else:
                return self.rec_one_direction_count(board, row_id + 1, col_id, direction)


        elif(board[row_id][col_id]=="B"):
            return 0

        elif(board[row_id][col_id]=="p"):
            return 1

    def numRookCaptures(self, board):
        r_row = r_col = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'R':
                    r_row, r_col = row, col

        count = 0

        directions = ['up', 'down', 'left', 'right']

        for direction in directions:
            count += self.rec_one_direction_count(board, r_row, r_col, direction)

        return count





sol = Solution()
board1 = [[".",".",".",".",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".","R",".",".",".","p"],
          [".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".","p",".",".",".","."],
          [".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".","."]]
print(sol.numRookCaptures(board1))


