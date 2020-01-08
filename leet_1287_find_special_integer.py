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




# nums1 = [1,2,3,3]

nums1 = [9057,10002,13452,13452,13452,14042,14141,14448,60395,95081]

print(find_special_integer3(nums1))