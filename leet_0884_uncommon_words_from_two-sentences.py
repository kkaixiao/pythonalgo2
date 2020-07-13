"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word
consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the
other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.
"""

import collections


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        A.extend(B.split(' '))
        d = dict(collections.Counter(A))
        res = []
        for k, v in d.items():
            if k != '' and v == 1:
                res.append(k)

        return res

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        A.extend(B.split(' '))
        d = dict()
        for letter in A:
            d[letter] = d.get(letter, 0) + 1

        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)

        return res

    # this is really a slow method
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c = Counter(A.split() + B.split())
        res = []
        for i in c:
            if c[i] == 1:
                res.append(i)

        return res

    # one line
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [k for k, v in dict(Counter((A + " " + B).split(" "))).items() if v == 1]