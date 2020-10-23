"""
Given an array nums of n integers and an integer target, find three integers in nums such that
the sum is closest to target. Return the sum of the three integers. You may assume that each
input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return

        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp_sum = nums[i] + nums[left] + nums[right]
                if abs(tmp_sum - target) < abs(res - target):
                    res = tmp_sum
                if tmp_sum < target:
                    left += 1
                elif tmp_sum > target:
                    right -= 1
                elif tmp_sum == target:
                    return tmp_sum

        return res