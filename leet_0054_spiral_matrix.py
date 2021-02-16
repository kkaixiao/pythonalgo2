"""
Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        lst = []

        while matrix and (len(matrix) > 1):

            lst += matrix.pop(0)
            r = len(matrix)

            l = len(matrix[0])
            newmat = [[0 for i in range(r)] for j in range(l)]
            for i in range(l):
                for j in range(r):
                    newmat[i][j] = matrix[j][l - i - 1]

            matrix = [[0 for i in range(r)] for j in range(l)]

            matrix = newmat
        lst += matrix.pop(0)

        return lst