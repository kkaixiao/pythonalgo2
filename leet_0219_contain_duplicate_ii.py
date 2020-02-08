"""
Given an array of integers and an integer k, find out whether there are two distinct indices
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j
is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict_nums = dict()
        for i in range(len(nums)):
            curr_arr = dict_nums.get(nums[i], [])
            curr_arr.append(i)
            dict_nums[nums[i]] = curr_arr

        # print(dict_nums)

        for _, v in dict_nums.items():
            if len(v) > 1:
                pre_idx = v[0]
                for idx in range(1, len(v)):
                    print(pre_idx, v[idx])
                    if abs(pre_idx - v[idx]) <= k:
                        return True
                    pre_idx = v[idx]

        return False


    def containsNearbyDuplicate2(self, nums, k):
        if len(set(nums)) == len(nums):
            return False

        for i in range(len(nums)-1):
            if nums[i] in nums[i + 1:i + 1 + k]:
                return True
        return False


#
# nums1 = [1,0,1,1]
# k1 = 1

nums1 = [1,2,3,1,2,3]
k1 = 2

mysol = Solution()
print(mysol.containsNearbyDuplicate(nums1, k1))