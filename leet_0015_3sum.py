"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        # let's fix on this index, set its negative value as objective
        for i in range(len(nums) - 2):
            # ignore repeating values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            obj = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == obj:
                    # found one, and add into result list
                    res.append([nums[i], nums[left], nums[right]])

                    # we need to check if any item is repeating
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # move the left and right pointers since one is found
                    left += 1
                    right -= 1

                # move left or right pointer once each
                elif nums[left] + nums[right] < obj:
                    left += 1
                else:
                    right -= 1

        return res