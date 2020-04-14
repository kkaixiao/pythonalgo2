
"""
Given a non-empty array of integers, return the third maximum number in this array. If it
does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

# for heap to be used
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))
        nums.sort()

        if len(nums) >= 3:
            return nums[len(nums) - 3]
        else:
            return nums[len(nums) - 1]

    # withou sort approach
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)

        nums = set(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))

        return max(nums)

    # use heap



    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        for n in nums:
            heapq.heappush(heap, -n)
        for i in range(1,3):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

