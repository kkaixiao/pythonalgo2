"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1
does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from itertools import product


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []

        d_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        letters = []

        for digit in digits:
            letters.append(d_map[digit])

        prod = list(product(*letters))

        for i in range(len(prod)):
            prod[i] = ''.join(prod[i])

        return prod


# 2nd solution without using itertools
class Solution(object):
    def letterCombinations(self, digits):
        res = []
        d_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        for i, c in enumerate(digits):
            if i == 0:
                for d in d_map[c]:
                    res.append(d)
            else:
                newRes = []
                for d in d_map[c]:
                    for s in res:
                        newRes.append(''.join([s, d]))

                res = newRes
        return res