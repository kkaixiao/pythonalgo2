"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both
would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means
not empty), and a number n, return if n new flowers can be planted in it without violating the
no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        countPlots = 0
        idxOfOne = []

        for i in range(len(flowerbed)):
            if flowerbed[i]:
                idxOfOne.append(i)

        # case when no '1' present
        if len(idxOfOne) == 0:
            countPlots = int((len(flowerbed) + 1) // 2)
            if countPlots >= n:
                return True
            else:
                return False
        # case for the first item is not 1
        pre = idxOfOne[0]
        if pre > 1:
            countPlots += int(pre // 2)
        if countPlots >= n:
            return True

        for j in range(1, len(idxOfOne)):
            distance = idxOfOne[j] - pre

            if distance > 3:
                countPlots += int(distance // 2 - 1)
            if countPlots >= n:
                return True
            pre = idxOfOne[j]
        last = len(flowerbed) - idxOfOne[-1]

        # case for the last item is not 1
        if last > 2:
            countPlots += int(last // 2)

        if countPlots >= n:
            return True
        return False

    # a smart method, but not as fast as the above
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        augmentedFlowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(len(flowerbed)):
            if sum(augmentedFlowerbed[i:i+3]) == 0:
                count += 1
                augmentedFlowerbed[i+1] = 1

        return True if count>=n else False