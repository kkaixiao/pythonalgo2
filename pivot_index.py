'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to
the sum of the numbers to the right of the index.If no such index exists, we should return -1.
If there are multiple pivot indexes, you should return the left-most pivot index.
Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Note:
The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
'''

def pivot_index(nums):
    left = 0
    right = sum(nums) - nums[0]

    if len(nums) == 0:
        return -1

    if left == right:
        return 0

    for i in range(0, len(nums)-1):
        left += nums[i]
        right -= nums[i+1]
        if left == right:
            return i + 1

    return -1


my_nums = [1, 7, 3, 6, 5, 6]


print(pivot_index(my_nums))