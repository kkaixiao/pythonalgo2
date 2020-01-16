'''
Given a non-empty array of integers, every element appears twice except for one. Find that single
one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra
memory?

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
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    while len(nums) > 0:
        try:
            tmp_ndx = nums.index(nums[0], 1, len(nums))
            if tmp_ndx >= 0:

                nums.pop(tmp_ndx)
                nums.pop(0)

        except ValueError:
            return nums[0]



def single_num_set(nums):
    print(set(nums))
    return sum(nums) - sum(set(nums))



def single_num_recursion(nums):

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    try:
        nums.pop(nums.index(nums[0], 1, len(nums)))
    except ValueError:
        return nums[0]
    nums.pop(0)
    return single_num_recursion(nums)


arr1 = [2,5,2,5,1]
arr2 = [4,1,2,1,2]
arr3 = [2,5,2,8,5,8,9]
arr4 = [2, 2, 1]
arr5 = []


# print(single_num_xor(arr2))
# print(single_num_index(arr4))
# print(single_num_set(arr3))
print(single_num_recursion(arr3))