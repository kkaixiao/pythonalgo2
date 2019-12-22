#Leetcode.num = 35. Search Insert Position
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Example 1:
Input: [1,3,5,6], 5
Output: 2
"""

def search_insert1(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return i+1


def search_insert2(nums, target):
    return nums.index(target) if target in nums else search_insert2_sub(nums, target)

def search_insert2_sub(nums, target):
    for i in range(len(nums)):
        if nums[i] > target:
            return i
    return i + 1


nums1 = [1,3,5,6]
target1 = 6

print(search_insert2(nums1, target1))