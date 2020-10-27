"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in
nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the
sum of target.

Notice that the solution set must not contain duplicate quadruplets.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []


Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4:
            return []
        res = []

        nums.sort()
        for ai in range(n - 3):
            # if same with prior number, go to the next index
            if ai > 0 and nums[ai] == nums[ai - 1]: continue

            # if the number is too large, finish the whole search
            if nums[ai] + 3 * nums[ai + 1] > target: break

            # if the number is too small, go for a higher number (next index)
            if nums[ai] + 3 * nums[-1] < target: continue
            for bi in range(ai + 1, n - 2):
                # if same with prior number, go to the next index
                if bi > ai + 1 and nums[bi] == nums[bi - 1]: continue

                # if the number is too large, finish the search in this loop
                if nums[ai] + nums[bi] + 2 * nums[bi + 1] > target: break

                # if the number is too small, go for a higher number
                if nums[ai] + nums[bi] + 2 * nums[-1] < target: continue

                # set intial index for c and d
                ci, di = bi + 1, n - 1
                while ci < di:
                    sum_res = nums[ai] + nums[bi] + nums[ci] + nums[di]
                    if sum_res == target:
                        # found one, append to result
                        res.append([nums[ai], nums[bi], nums[ci], nums[di]])

                        # increase index for c if the value is same as the next
                        while ci < di and nums[ci] == nums[ci + 1]:
                            ci += 1

                        # decrease index for d if the value is same as the prior
                        while ci < di and nums[di] == nums[di - 1]:
                            di -= 1
                        # normal increase and decrease for index of c and d
                        ci += 1
                        di -= 1

                    # change index for c and d based on value comparison
                    elif sum_res < target:
                        ci += 1
                    else:
                        di -= 1
        return res