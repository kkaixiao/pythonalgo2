"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the
array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""

def find_special_integer(nums):
    if len(nums) == 1:
        return nums[0]

    start_pointer = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[start_pointer]:
            end_pointer = i
            if (end_pointer - start_pointer + 1) > len(nums) / 4:
                return nums[i]
        else:
            start_pointer = i


# nums1 = [1,2,2,6,6,6,6,7,10]

nums1 = [1,2,3,3]
print(find_special_integer(nums1))