"""
Given scores of N athletes, find their relative ranks and the people with the top three
highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal",
"Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        sortedNums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)
        count = 0
        for i, _ in sortedNums:
            count += 1
            if count == 1:
                nums[i] = 'Gold Medal'
            elif count == 2:
                nums[i] = 'Silver Medal'
            elif count == 3:
                nums[i] = 'Bronze Medal'
            else:
                nums[i] = str(count)
        return nums



