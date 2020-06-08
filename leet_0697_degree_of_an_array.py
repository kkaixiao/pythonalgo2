"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as
the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has
the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
class Solution:
    # a slow solution
    def findShortestSubArray(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = str(numsDict.get(nums[i], '')) + str(i) + ','

        maxLen, minDiff = 0, 0
        for _, v in numsDict.items():
            aList = v[:-1].split(',')

            if len(aList) > maxLen:
                minDiff = int(aList[-1]) - int(aList[0])
                maxLen = len(aList)
            elif len(aList) == maxLen:
                if minDiff > int(aList[-1]) - int(aList[0]):
                    minDiff = int(aList[-1]) - int(aList[0])
        return minDiff + 1
