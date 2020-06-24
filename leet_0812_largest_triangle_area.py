"""
ou have a list of points in the plane. Return the area of the largest triangle that can be formed
by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""


class Solution:
    from itertools import combinations

    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calcTriangleArea(pint1, point2, point3):
            [x1, y1], [x2, y2], [x3, y3] = pint1, point2, point3

            # A = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2

            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        combin = combinations(points, 3)
        # print(combin)

        return max(calcTriangleArea(a, b, c) for a, b, c in combin)