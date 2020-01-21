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
    # try | exception with index search method # not good
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            try:
                idx = nums.index(target - nums[i], i+1, len(nums))
            except ValueError:
                continue

            if idx > 0:
                return [i, idx]

    # brutal force method # not good
    def twoSum2(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # hash table method （2-round) # better
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

    # hash table method （1-round) # much better
    def twoSum4(self, nums, target):
        nums_dict = {}
        for i in range(len(nums)):
            # if one key does not exist, we use default value of 0
            if nums_dict.get((target - nums[i]), 0) > 0:
                return [i, nums_dict[target - nums[i]]-1]

            # we increment value to set to a key/value pair
            nums_dict[nums[i]] = i+1

    # worst method by using combinations class, # Memory Limit Exceeded in leetcode#
    def twoSum5(self, nums, target):
        from itertools import combinations as combine

        for i in list(combine(nums, 2)):
            a, b = i
            if a + b == target:
                a_index = nums.index(a)
                nums[a_index] = None
                b_index = nums.index(b)
                return [a_index, b_index]

    # Recursion function, not so efficient
    def twoSum6(self, nums, target, rec_nums=[]):

        if not len(rec_nums):
            rec_nums = nums.copy()
            rec_nums.sort()

        if rec_nums[0] + rec_nums[-1] == target:
            a_index = nums.index(rec_nums[0])
            nums[a_index] = None
            b_index = nums.index(rec_nums[-1])
            return [a_index, b_index]

        if rec_nums[-1] + rec_nums[0] > target:
            rec_nums.pop()
            return self.twoSum6(nums, target, rec_nums)
        elif rec_nums[-1] + rec_nums[0] < target:
            rec_nums.pop(0)
            return self.twoSum6(nums, target, rec_nums)
        elif rec_nums[0] + rec_nums[-1] == target:
            a_index = nums.index(rec_nums[0])
            nums[a_index] = None
            b_index = nums.index(rec_nums[-1])
            return [a_index, b_index]


    # Recursion function with deque
    def twoSum7(self, nums, target, rec_nums=[]):
        from collections import deque

        if not len(rec_nums):
            rec_nums = nums.copy()
            rec_nums.sort()
            rec_nums = deque(rec_nums)

        if rec_nums[0] + rec_nums[-1] == target:
            a_index = nums.index(rec_nums[0])
            nums[a_index] = None
            b_index = nums.index(rec_nums[-1])
            return [a_index, b_index]

        if rec_nums[-1] + rec_nums[0] > target:
            rec_nums.pop()
            return self.twoSum7(nums, target, rec_nums)
        elif rec_nums[-1] + rec_nums[0] < target:
            rec_nums.popleft()
            return self.twoSum7(nums, target, rec_nums)
        elif rec_nums[0] + rec_nums[-1] == target:
            a_index = nums.index(rec_nums[0])
            nums[a_index] = None
            b_index = nums.index(rec_nums[-1])
            return [a_index, b_index]

nums1 = [11, 2, 7, 11]
target1 = 22

# nums1 = [3,2,4]
# target1 = 6

# nums1 = [11,2,7,14]
# target1 = 21

# nums1 = [3,2,3]
# target1 = 6

# nums1 = [3,2,95,4,-3, 72, 23, -5, 4]
# target1 = 92

sol1 = Solution()
print(sol1.twoSum7(nums1, target1))