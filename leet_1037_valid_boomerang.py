"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.



Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false


Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""


class Solution:

    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False

        angel1 = math.atan2(points[0][1] - points[1][1], points[0][0] - points[1][0])

        angel2 = math.atan2(points[1][1] - points[2][1], points[1][0] - points[2][0])

        angel3 = math.atan2(points[0][1] - points[2][1], points[0][0] - points[2][0])

        print(angel1, angel2, angel3)
        if (angel1 == math.pi and angel2 == math.pi) or (angel1 == math.pi and angel3 == math.pi) or (
                angel2 == math.pi and angel3 == math.pi):
            return False
        if (angel1 == 0 and angel2 == 0) or (angel1 == 0 and angel3 == 0) or (angel2 == 0 and angel3 == 0):
            return False

        return not (angel1 == angel2)


    def isBoomerang(self, points: List[List[int]]) -> bool:

        v1 = (points[0][1] - points[1][1], points[0][0] - points[1][0])
        v2 = (points[1][1] - points[2][1], points[1][0] - points[2][0])

        return v1 != (0, 0) and v2 != (0, 0) and v1[0] * v2[1] - v1[1] * v2[0] != 0