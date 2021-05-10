"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r, row in enumerate(board):
            for c, char in enumerate(row):
                if char == word[0]:
                    temp = char
                    board[r][c] = None
                    if self.search(board, word[1:], [r, c]):
                        return True
                    board[r][c] = temp
        return False

    def search(self, board, word, pos):
        if len(word) < 1: return True
        for dir in self.dirs:
            r = pos[0] + dir[0]
            c = pos[1] + dir[1]
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == word[0]:
                    temp = board[r][c]
                    board[r][c] = None
                    if self.search(board, word[1:], [r, c]):
                        return True
                    board[r][c] = temp
        return False
