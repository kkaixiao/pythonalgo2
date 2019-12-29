'''
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

'''


def contains_duplicate_ii1(nums, k):
    if len(set(nums)) == len(nums):
        return False
    for i in range(len(nums)-1):
        if nums[i] in nums[i + 1:i + 1 + k]:
            return True
    return False


def contains_duplicate_ii2(nums, k):
    mdict = {}
    for index, value in enumerate(nums):
        if (value in mdict) and (index - mdict[value] <= k):
            return True
        mdict[value] = index
    return False


# nums1 = [1,2,3,1]  # should return True
# k1 = 3
#
# nums1 = [1,2,3,4,5,6,7,8,9,9]  # should return True
# k1 = 3


nums1 = [13,23,1,2,3]  # should return False
k1 = 5
print(contains_duplicate_ii2(nums1, k1))
