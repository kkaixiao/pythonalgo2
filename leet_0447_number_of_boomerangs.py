"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of
points (i, j, k) such that the distance between i and j equals the distance between i and k
(the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of
points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


from itertools import permutations


class Solution:
    # the following solution time limit exceeded
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        perms = permutations(points, 3)
        for perm in perms:
            if self.isBommerangs(perm[0], perm[1], perm[2]):
                count += 1
        return count

    def isBommerangs(self, pointI, pointJ, pointK):
        ItoJ = (pointI[0] - pointJ[0]) ** 2 + (pointI[1] - pointJ[1]) ** 2
        ItoK = (pointI[0] - pointK[0]) ** 2 + (pointI[1] - pointK[1]) ** 2
        return ItoJ == ItoK


    # an O(N^2) solution using hastable
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p1 in points:
            D = dict()
            for p2 in points:
                distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if(distance in D):
                    res += D[distance]
                    D[distance] += 2
                else:
                    D[distance] = 2
        return res