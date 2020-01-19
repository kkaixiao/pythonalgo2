"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array
indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells
in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all
indices.



Example 1:
Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:
Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
"""

class Solution:
    def oddCells(self, n, m, indices):
        mat = [[0 for _ in range(m)] for _ in range(n)]
        for arr_inc in indices:
            for x in range(len(mat[arr_inc[0]])):
                mat[arr_inc[0]][x] += 1
            for arr in mat:
                arr[arr_inc[1]] += 1

        count = 0
        for i in range(n):
            for j in range(m):
                # if mat[i][j] % 2:
                #     count += 1
                count += mat[i][j] % 2

        return count


    def oddCells2(self, n, m, indices):
        row_count_array = [0] * n
        col_count_array = [0] * m
        for idx in indices:
            row_count_array[idx[0]] += 1
            col_count_array[idx[1]] += 1

        row_cnt = sum([1 for r in row_count_array if r % 2 == 1])

        col_cnt = sum([1 for c in col_count_array if c % 2 == 1])

        odd_number = row_cnt * m + (n - row_cnt) * col_cnt - row_cnt * col_cnt

        return odd_number


oddCells1 = Solution()


print(oddCells1.oddCells(2, 3, [[0,1],[1,1]]))
#
# print(oddCells1.oddCells2(2, 2, [[1,1],[0,0]]))