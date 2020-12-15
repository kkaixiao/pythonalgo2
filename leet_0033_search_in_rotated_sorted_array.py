"""
You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7]
might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rot_idx = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                rot_idx = i
                break
            prev = nums[i]

        new_nums = []
        for num in nums[rot_idx:]:
            new_nums.append(num)
        for num in nums[:rot_idx]:
            new_nums.append(num)

        l, r = 0, len(new_nums) - 1
        while l <= r:
            m = (l + r) // 2
            if new_nums[m] == target:
                return (m + rot_idx) % len(nums)
            elif new_nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1

