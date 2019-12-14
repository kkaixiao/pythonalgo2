'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''


def single_num_xor(nums):
    res = 0
    for num in nums:
        res ^= num
    return res


def single_num_index(nums):
    i = 0
    while len(nums) > 0:
        try:
            if nums[i+1:].index(nums[i]) >= 0:
                nums.pop(nums[i+1:].index(nums[i]))
                nums.pop(i)
                i += 1
        except ValueError:
            return nums[i]



arr1 = [2,5,2,1,5]
arr2 = [4,1,2,1,2]
arr3 = [2,5,2,1,5]


# print(single_num_xor(arr2))
print(single_num_index(arr1))
