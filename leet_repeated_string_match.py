"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B
is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is
not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution:
    # Output Limit Exceeded
    def repeatedStringMatch(self, A: str, B: str) -> int:
        count = 1
        addStr = ''
        for i in range(len(B) // len(A) + 2):
            addStr += A

            if addStr.find(B) > -1:
                return count
            count += 1

        return -1

    def repeatedStringMatch(self, A: str, B: str) -> int:

        for i in range(1, len(B) // len(A) + 3):
            if B in A * i:
                return i

        return -1

    # this will be super fast
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if len(set(B)) > len(set(A)):
            return -1

        # the repeat number will be either len(B)/len(A) or len(B)/len(A) +1

        repeatNum = ceil(len(B) / len(A))

        repeatNums = [repeatNum, repeatNum + 1]
        # print(repeatNums)

        for i in repeatNums:
            if B in A * i:
                return i

        return -1