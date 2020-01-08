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
    len_limit = len(nums) / 4 - 1

    for i in range(1, len(nums)):
        if nums[i] == nums[start_pointer]:
            if (i - start_pointer) > len_limit:
                return nums[i]
        else:
            start_pointer = i



# made by Liu Jun, quite a smart approach
def findSpecialInteger(x):
    if len(x) == 1:
        return 1
    list_lens = int(len(x) / 4 + 1)
    i = 1
    while i < len(x):
        if x.count(x[i]) < list_lens:
            i += list_lens
        else:
            return x[i]


from math import floor
def find_special_integer3(nums):
    if len(nums) == 1 or len(nums) == 2:
        return nums[0]

    step = floor(len(nums) / 4)

    for i in range(len(nums) - step):
        if nums[i] == nums[i + step]:
            return nums[i]


# The answer must be one of (nums[0], nums[l/4], nums[l/2], nums[l*3/4]) where l is the length
# of nums. What we should do is to find the start and end points of each of the number, we find
# the special number if (end_pointer - start_pointer + 1) > 0.25

def find_special_integer4(nums):
    partition_length = len(nums)//4
    for i in range(4):
        start_end = find_start_end(nums, i * partition_length)
        if (start_end[1] - start_end[0] + 1) > len(nums) / 4:
            return nums[i * partition_length]


def find_start_end(nums, idx):
    start_pointer = end_pointer = idx
    while 0 < start_pointer:
        if nums[start_pointer] == nums[start_pointer - 1]:
            start_pointer -= 1
        else:
            break

    while end_pointer < len(nums)-1:
        if nums[end_pointer] == nums[end_pointer+1]:
            end_pointer += 1
        else:
            break
    return (start_pointer, end_pointer)

# nums1 = [1,2,3,3]
# nums1 = [1]
# nums1 = [10002,10002,13452,13452,14141,14141,14141,14448,60395,76328,95081]
nums1 = [2,3,5,5, 9]

print(find_special_integer4(nums1))