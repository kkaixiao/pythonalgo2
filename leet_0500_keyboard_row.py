"""
Given a List of words, return the words that can be typed using letters of alphabet on only
one row's of American keyboard like the image below.



Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        upperRow, midRow, lowerRow = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        res = []
        for word in words:
            d = {'u': 0, 'm': 0, 'l': 0}
            for c in set(word.lower()):
                if c in upperRow:
                    d['u'] = 1
                elif c in midRow:
                    d['m'] = 1
                elif c in lowerRow:
                    d['l'] = 1
            count = 0
            for _, v in d.items():
                count += v

            if count == 1:
                res.append(word)

        return res

    # without dictionary
    def findWords(self, words: List[str]) -> List[str]:
        upperRow, midRow, lowerRow = 'qwertyuiop', 'asdfghjkl', 'zxcvbnm'
        res = []
        for word in words:
            l = []
            for c in set(word.lower()):
                if c in upperRow:
                    l.append(1)
                elif c in midRow:
                    l.append(2)
                elif c in lowerRow:
                    l.append(3)

            if len(set(l)) == 1:
                res.append(word)

        return res