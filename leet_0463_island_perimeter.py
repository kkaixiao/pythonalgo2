"""
ou are given a map in form of a two-dimensional integer grid where 1 represents land and 0
represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely
surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the
island). One cell is a square with side length 1. The grid is rectangular, width and height
don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = col = 0
        count = 0
        while row < len(grid):

            while col < len(grid[row]):

                if grid[row][col] == 1:

                    if ((col - 1 >= 0 and grid[row][col - 1] == 0) or col - 1 < 0):
                        count += 1

                    if (col + 1 >= len(grid[row]) or (col + 1 < len(grid[row]) and grid[row][col + 1] == 0)):
                        count += 1

                    if (row - 1 < 0 or grid[row - 1][col] == 0):
                        count += 1

                    if (row + 1 >= len(grid) or grid[row + 1][col] == 0):
                        count += 1
                col += 1

            row += 1
            # get back to the first column
            col = 0

        return count


    # 2nd solution

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    count += 4
                    if col and grid[row][col-1]:
                        count -= 2

                    if row and grid[row-1][col]:
                        count -= 2

        return count