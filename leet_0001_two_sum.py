"""
Given an array of integers, return indices of the two numbers such that they add up to a
specific target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            idx = 0
            try:
                idx = nums.index(target - nums[i], i+1, len(nums))
            except ValueError:
                continue

            if idx > 0:
                return [i, idx]

    def twoSum2(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum3(self, nums, target):
        nums_copy = nums.copy()
        nums.sort()
        for start_idx in range(len(nums) - 2):
            for end_idx in range(len(nums) - 1, start_idx, -1):
                print(start_idx, end_idx)
                if nums[start_idx] + nums[end_idx] == target:

                    return [nums_copy.index(nums[start_idx]), nums_copy.index(nums[end_idx])]





# nums1 = [2, 7, 11, 15]
# target1 = 9

# nums1 = [3,2,4]
# target1 = 6

nums1 = [2,7,11,14]
target1 = 9
sol1 = Solution()
print(sol1.twoSum3(nums1, target1))