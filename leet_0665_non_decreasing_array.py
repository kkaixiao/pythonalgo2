"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by
modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such
that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        countDec = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:

                if countDec == 1:
                    return False

                countDec += 1
                # for a case like: [4,5,2,3], when i = 2, 2<4, we can replace 2 by 5
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]

        return True