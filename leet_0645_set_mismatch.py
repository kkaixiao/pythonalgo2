"""
he set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one
of the numbers in the set got duplicated to another number in the set, which results in repetition
of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to
firstly find the number occurs twice and then find the number that is missing. Return them in the
form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

class Solution:
    # a fairly slow solution with has table
    def findErrorNums(self, nums: List[int]) -> List[int]:

        mapDict = {}
        for i in range(len(nums)):
            mapDict[i+1] = 0

        for num in nums:
            mapDict[num] += 1
        rep, miss = 0, 0
        for k,v in mapDict.items():
            if v == 2:
                rep = k
            if v == 0:
                miss = k
        return [rep, miss]


    # Time Limit Exceeded for this approach
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep, miss, c = 0, 0, 0

        while (not rep or not rep) or c < len(nums):
            if nums.count(c+1) == 0:
                miss = c+1
            if nums.count(c+1) == 2:
                rep = c+1
            c += 1
        return [rep, miss]


    # a fast method by using number difference between sum of list and set
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sumPerfect, sumOfSet = int(n*(n+1)/2), sum(set(nums))
        return [sum(nums) - sumOfSet, sumPerfect - sumOfSet]