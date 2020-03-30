"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j),
inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
"""

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray:

    def __init__(self, nums):
        self.arrays = []
        sub_sum = 0

        for number in nums:
            sub_sum += number
            self.arrays.append(sub_sum)

    def sumRange(self, i, j):
        if i == 0:
            return self.arrays[j]
        else:
            return self.arrays[j] - self.arrays[i - 1]

