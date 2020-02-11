"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is
missing from the array.


Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant
extra space complexity?
"""

class Solution:
    def missingNumber(self, nums):
        for i in range(len(nums) + 1):
            if i not in nums:
                return i


    def missingNumber2(self, nums):
        nums_dict = dict()
        for i in range(len(nums)+1):
            nums_dict[i] = 1

        for num in nums:
            nums_dict[num] -= 1

        for k, v in nums_dict.items():
            if v == 1:
                return k


    def missingNumber3(self, nums):
        # sum_with_missing = len(nums) * (1 + len(nums)) // 2
        # return sum_with_missing - sum(nums)
        return len(nums) * (1 + len(nums)) // 2 - sum(nums)

nums1 = [9,6,4,2,3,5,7,0,1]

mysol = Solution()
print(mysol.missingNumber3(nums1))