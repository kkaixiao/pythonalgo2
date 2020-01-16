
"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O"
characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or
diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and
column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return
"Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially
empty and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X O"
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    " OX"

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "


Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""


def tictactoe(moves):

    a_plays = []
    b_plays = []

    for i in range(len(moves)):
        if i % 2:
            b_plays.append(moves[i])
        else:
            a_plays.append(moves[i])

    if judge_win(a_plays):
        return 'A'

    if judge_win(b_plays):
        return 'B'

    if not judge_win(a_plays) and not judge_win(b_plays):
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'


def judge_win(moves):
    if len(moves) < 3:
        return False

    v_dict = {}
    h_dict = {}

    for move in moves:
        v_dict[move[0]] = v_dict.get(move[0], 0) + 1
        h_dict[move[1]] = h_dict.get(move[1], 0) + 1

    for _, v in v_dict.items():
        if v == 3:
            return True

    for _, v in h_dict.items():
        if v == 3:
            return True

    diagonal1 = diagonal2 = 0

    diagonal_points1, diagonal_points2 = [[0, 0], [2, 2]], [[0, 2], [2, 0]]

    has_center = False

    for move in moves:
        if move in diagonal_points1:
            diagonal1 += 1

        if move in diagonal_points2:
            diagonal2 += 1

        if move == [1, 1]:
            has_center = True

    if (diagonal1 == 2 or diagonal2 == 2) and has_center:
        return True

    return False


import re


def tictactoe3(moves):
    grid = [' '] * 16
    for i, (y, x) in enumerate(moves):
        grid[4 * y + x] = p = 'AB'[i & 1]

        if re.search(f"{p}{{3}}|({p}..){{3}}|({p}...){{3}}|({p}....){{3}}", ''.join(grid)): return p

    return ('Pending', 'Draw')[len(moves) == 9]

# moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]]  # A

# moves1 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]  # B

moves1 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]  # Draw
#
# moves1 = [[0,0],[1,1]]  # Pending

# moves1 = [[1,2],[1,0],[0,0],[0,1],[2,1]]  # Pending
#
# moves1 = [[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]  # A
#
# moves1 = [[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]  # B
#
# moves1 = [[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]  # B
#
# moves1 = [[1,0],[2,2],[0,1],[0,2],[2,1],[1,1],[0,0],[2,0]]  # B

# print(tictactoe(moves1))

print(tictactoe3(moves1))
