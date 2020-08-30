"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only
if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to
another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is
equivalent to dominoes[j].



Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

"""


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        d = {}

        for domino in dominoes:
            k = 0
            if domino[0] < domino[1]:
                k = domino[0] * 10 + domino[1]
            else:
                k = domino[1] * 10 + domino[0]

            d[k] = d.get(k, 0) + 1

        def calcCombination(n):
            res = 0
            for i in range(1, n):
                res += i
            return res

        cnt = 0
        for _, v in d.items():
            if v > 1:
                cnt += calcCombination(v)

        return cnt



