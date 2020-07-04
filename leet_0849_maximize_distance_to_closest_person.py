"""
n a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is
empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is
maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.


Constraints:

2 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""


class Solution:
    # first method, very slow
    def maxDistToClosest(self, seats: List[int]) -> int:
        idxs = []
        for i in range(len(seats)):
            if seats[i]:
                idxs.append(i)
        maxInterSpace = 0
        if len(idxs) > 1:
            for j in range(len(idxs) - 1):
                maxInterSpace = max((idxs[j + 1] - idxs[j]), maxInterSpace)
        maxInterSpace = maxInterSpace // 2

        return max(maxInterSpace, idxs[0], len(seats) - idxs[-1] - 1)


    # two poiners approach, much faster
    def maxDistToClosest(self, seats: List[int]) -> int:

        left = right = res = 0
        for right in range(len(seats)):
            if seats[right] == 1 or right == len(seats) - 1:
                temp = right - left
                res = max(res, temp if seats[left] * seats[right] == 0 else temp // 2)
                left = right
        return res
