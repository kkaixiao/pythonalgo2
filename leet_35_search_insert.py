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

'''
We know the array is sorted, so we can reduce the search to O(logN) via binary search. 
If not found, i>=j then we need to compare target with the nums[i], 
return i + 1 if the target is bigger (insert after) or i otherwise (insert before).
'''



def search_insert3(nums, target):
    # we set start_ndx and end_ndx the starting and ending index of a string
    # remember these two indices will get changed when the iteration runs
    start_ndx, end_ndx = 0, len(nums)-1

    # the iteration condition is end_ndx is greater than the start_ndx
    while start_ndx < end_ndx:
        # select an index in the middle
        mid = int(start_ndx + (end_ndx-start_ndx)/2)

        # we have already found the value in the middle
        if target == nums[mid]:
            return mid

        # in the case where target is bigger than the middle value
        # in order to accelerate searching speed, end_ndx now walks for the distance of int((mid-start_ndx)/2),
        # instead of the previous constant 1, however, we should consider the cases when int((mid-start_ndx)/2) == 0
        # in this situation, endless iteration may happen

        if target > nums[mid]:
            start_ndx = mid + int((mid-start_ndx)/2) + 1


        # if target is smaller than or equal to the middle value
        # in order to accelerate searching speed, end_ndx now walks for the distance of int((end_ndx-mid)/2),
        # instead of the previous constant 1, however, we should consider the cases when int((end_ndx-mid)/2) == 0
        # in this situation, endless iteration may happen
        else:
            end_ndx = mid - int((end_ndx-mid)/2) + 1


    return start_ndx + 1 if target > nums[start_ndx] else start_ndx

nums1 = [1,3,5,6,7, 9, 11, 13, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 33, 35, 37, 39, 40, 41, 42, 43]
target1 = 8

print(search_insert3(nums1, target1))