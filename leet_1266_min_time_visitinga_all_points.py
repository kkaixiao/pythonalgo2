"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to
find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally
(it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.


Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5


Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""


class Solution:
    # def minTimeToVisitAllPoints(self, points):

    def minTimeToVisitAllPoints(self, points):
        start_point = points[0]
        seconds = 0

        for i in range(1, len(points)):
            next_point = points[i]
            seconds += self.calculate_min_time_to_visit_one_step(start_point, next_point)
            start_point = next_point

        return seconds


    def calculate_min_time_to_visit_one_step(self, point_start, point_destination):
        point_start[0] = min(1000, point_start[0])
        point_start[1] = min(1000, point_start[1])
        point_destination[0] = min(1000, point_destination[0])
        point_destination[1] = min(1000, point_destination[1])

        # get diagonal point coordinate
        diagonal_step_point = self.find_diagonal_line_point(point_start, point_destination)

        # calculate seconds of diagonal line
        seconds = abs(diagonal_step_point[0] - point_start[0])

        # if the diagonal goes to a point share x-coordinate of destination,
        # we calculate and increment seconds with distance in y-axis
        if diagonal_step_point[0] == point_destination[0]:
            seconds += abs(point_destination[1] - diagonal_step_point[1])

        # otherwise we calculate and increment seconds with distance in x-axis
        else:
            seconds += abs(point_destination[0] - diagonal_step_point[0])

        return seconds


    def find_diagonal_line_point(self, point_start, point_destination):
        # we need to go diagonally to a point where either x-coordinate or y-coordinate is the same as
        # that of point_destination.
        # in this approach, we should go to a point whose distances to point_start along x-axis and y-axis
        # are the same.
        # so, we can get two points at first:
        # case 1: point_destination[1]-point_start[1] = unknown_x - point_start[0]
        # so, unknown_x = point_destination[1]-point_start[1] + point_start[0]
        # case 2: unknown_y - point_start[1] = point_destination[0] - point_start[0]
        # so, unknown_y = point_destination[0] - point_start[0] + point_start[1]

        diagonal_x = point_destination[1] - point_start[1] + point_start[0]
        diagonal_y = point_destination[0] - point_start[0] + point_start[1]

        if abs(diagonal_x - point_start[0]) > abs(diagonal_y - point_start[1]):
            return [point_destination[0], diagonal_y]
        else:
            return [diagonal_x, point_destination[1]]


points1 = [[1,1],[3,4],[-1,0]]
# points1 = [[3,2],[-2,2]]
#
# points1 = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]
this_obj = Solution()

print(this_obj.minTimeToVisitAllPoints(points1))

