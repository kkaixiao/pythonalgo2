"""
Count the number of segments in a string, where a segment is defined to be a contiguous
sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
class Solution:
    def countSegments(self, s: str) -> int:
        if s == '':
            return 0

        res, start = 0, False

        for char in s:
            if char != ' ':
                if not start:
                    start, res = True, res + 1
            else:
                if start:
                    start = False

        return res


