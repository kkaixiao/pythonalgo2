"""
You are given a string representing an attendance record for a student. The record only contains
the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""


class Solution:
    # this could be better
    def checkRecord(self, s: str) -> bool:
        absent, late = 0, 0
        prev = ''
        for c in s:
            if c == 'A':
                absent += 1
            if c == 'L':
                if prev != 'L':
                    late = 1
                else:
                    late += 1

            if absent > 1 or late > 2:
                return False

            prev = c
        return True

    # this could be slower
    def checkRecord(self, s: str) -> bool:
        absentNum, lateContNum = 0, 0
        prev = ''
        for c in s:
            if c == 'A':
                absentNum += 1
            if c == 'L' and prev != 'L':
                lateContNum = 1
            if c == 'L' and prev == 'L':
                lateContNum += 1
            prev = c
            if absentNum > 1 or lateContNum > 2:
                return False
        return True

    # a simpler method
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s:
            return False
        countLate = 0
        for c in s:
            if c == "A":
                countLate += 1

        return countLate < 2

    # one line
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s