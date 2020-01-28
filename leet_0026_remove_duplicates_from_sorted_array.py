"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2
respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to
0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array
will be known to the caller as well.

Internally you can think of this:
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        ret_list = []
        ret_list.append(nums[0])
        index_i = 0

        for i in range(1, len(nums)):
            if nums[i] not in ret_list:
                ret_list.append(nums[i])
                nums[index_i + 1] = nums[i]
                index_i += 1

        print(ret_list)
        return len(ret_list)


    def removeDuplicates2(self, nums):
        if not nums:
            return 0

        len_nums = len(nums)
        prev_num = nums[0]
        nums.append(prev_num)

        for i in range(1, len_nums):
            if prev_num != nums[i]:
                nums.append(nums[i])
            prev_num = nums[i]

        nums.reverse()
        for _ in range(len_nums):
            nums.pop()
        nums.reverse()



# nums1 = [1,1,2]
nums1 = [0,0,1,1,1,2,2,3,3,4]
mysolution = Solution()
print(mysolution.removeDuplicates2(nums1))