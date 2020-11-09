"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed
parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n):
        def dfs(s, res, open_cnt, close_cnt):
            if open_cnt == 0 and close_cnt == 0:
                res.append(s)
            if open_cnt > 0:
                dfs(s + '(', res, open_cnt - 1, close_cnt)
            if open_cnt < close_cnt:
                dfs(s + ')', res, open_cnt, close_cnt - 1)
            return

        res = []
        dfs('', res, n, n)
        return res