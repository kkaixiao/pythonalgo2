"""
Given an array of size n, find the majority element. The majority element is the element that
appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        dict_nums = {}
        for num in nums:
            if dict_nums.get(num, 0) >= len(nums)//2:
                return num
            else:
                dict_nums[num] = dict_nums.get(num, 0) + 1

    def majorityElement2(self, nums):
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
            if dict_nums[num] > len(nums) // 2:
                return num


    def majorityElement3(self, nums):
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1

        for k, v in dict_nums.items():
            if v > len(nums)//2:
                return k

        return -1

    def majorityElement4(self, nums):
        nums.sort()
        return nums[len(nums)//2]



input1 = [2,2,1,1,1,1,2]

sol = Solution()

print(sol.majorityElement4(input1))
