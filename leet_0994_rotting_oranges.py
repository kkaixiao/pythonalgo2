"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is
impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting
only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid):
        row_num = len(grid)
        col_num = len(grid[0])
        rottens = []
        freshes = []
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == 2:
                    rottens.append([i,j])
                elif grid[i][j] == 1:
                    freshes.append([i,j])
        count = 0

        while len(freshes) > 0:
            if self.spread_once(rottens, freshes) == 0:
                return -1
            else:
                count += 1

        return count


    def spread_once(self, rotten_array, fresh_array):
        removed_items = []
        count = 0
        for rotten_item in rotten_array:
            possible_neighbors = [[rotten_item[0]+1, rotten_item[1]], [rotten_item[0]-1, rotten_item[1]],
                                  [rotten_item[0], rotten_item[1]+1], [rotten_item[0], rotten_item[1]-1]]

            for neighbor in possible_neighbors:
                if neighbor in fresh_array:
                    fresh_array.remove(neighbor)
                    removed_items.append(neighbor)
                    count += 1

        for removed_item in removed_items:
            if removed_item not in rotten_array:
                rotten_array.append(removed_item)

        return count






# grid1 = [[2,1,1],
#          [1,1,0],
#          [0,1,1]]
# grid1 = [[0,2]]
grid1 = [[2,1,1],[0,1,1],[1,0,1]]
# grid1 = [[2,1,1],
#          [1,1,0],
#          [0,1,1],
#          [2,1,1]]
mysolution = Solution()
print(mysolution.orangesRotting(grid1))