#Leetcode.num = 704. Binary Search
"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""


def binary_search(nums, target):
    start_idx, end_idx = 0, len(nums)-1

    while start_idx <= end_idx:
        mid = int(start_idx + (end_idx-start_idx)/2)

        if target == nums[mid]:
            return mid

        if target > nums[mid]:
            start_idx = mid + 1
        else:
            end_idx = mid - 1

    return -1


def binary_search_recur_body(nums, target, start_idx=0, end_idx=1):
    mid_idx = int((start_idx + end_idx) / 2)

    if target == nums[mid_idx]:
        return mid_idx
    if start_idx >= end_idx:
        return -1
    else:
        if target > nums[mid_idx]:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx -1
        return binary_search_recur_body(nums, target, start_idx, end_idx)


def binary_search_recur(nums, target):
    return binary_search_recur_body(nums, target, 0, len(nums)-1)

nums1 = [1,2, 3, 4, 5, 7]
target1 = 5

print(binary_search_recur(nums1, target1))
