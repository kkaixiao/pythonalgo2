"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the
 resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping
[1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example,
inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""


class Solution:
    # negate only when two corresponding points equal
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        w = len(A[0])
        for row in A:

            for i in range(w // 2):
                if row[i] == row[w - i - 1]:
                    row[i], row[w - i - 1] = row[i] ^ 1, row[w - i - 1] ^ 1

        if len(A[0]) % 2:
            for row in A:
                row[w // 2] = row[w // 2] ^ 1

        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:

            lHalf, isOdd = len(row)//2, len(row)%2

            row[:lHalf], row[lHalf+isOdd:] = row[lHalf+isOdd:][::-1], row[:lHalf][::-1]

            for i in range(len(row)):
                row[i] = row[i]^1

        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            row[:] = row[::-1]

            res.append([1 - x for x in row])

        return res

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for row in A:

            row[:] = row[::-1]
            for i in range(len(row)):
                # use x^1 instead of 1-x
                row[i] = row[i]^1

        return A

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        return [[x^1 for x in row[::-1]] for row in A]

    # fastest solution
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x:x^1, row[::-1])) for row in A]