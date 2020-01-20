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
        if len(nums) == 2:
            return [0, 1]

        nums_dict = {}

        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for i in range(len(nums)):
            first_num = nums[i]
            nums_dict[first_num] = nums_dict.get(first_num) - 1
            second_num = target - first_num
            if nums_dict.get(second_num, 0) > 0:
                return [i, nums[i+1:].index(second_num)+i+1]








# nums1 = [11, 2, 7, 11]
# target1 = 22

# nums1 = [3,2,4]
# target1 = 6

# nums1 = [11,2,7,14]
# target1 = 21

# nums1 = [3,2,3]
# target1 = 6

nums1 = [3,2,95,4,-3]
target1 = 92

sol1 = Solution()
print(sol1.twoSum3(nums1, target1))