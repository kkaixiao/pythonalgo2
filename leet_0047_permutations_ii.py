"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique
permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(results, curr_result):
            if len(curr_result) == len(nums):
                results.append(curr_result[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                if nums[i] != "#":
                    curr_num, nums[i] = nums[i], "#"
                    curr_result.append(curr_num)
                    backtrack(results, curr_result)
                    curr_result.pop()
                    nums[i] = curr_num

        res = []
        backtrack(res, [])
        return res