"""
Given an array of integers nums sorted in ascending order, find the starting and ending position
of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = [-1, -1]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return [-1, -1]

        res[0] = left

        left, right = left, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        res[-1] = left - 1 if nums[left] != target else left

        return res
