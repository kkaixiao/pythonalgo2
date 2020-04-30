"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

class Solution:
    # first intuitive solution, slow!
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countDict = []
        tempCount = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                tempCount += nums[i]
            else:
                countDict.append(tempCount)
                tempCount = nums[i]

        countDict.append(tempCount)

        return max(countDict)

    # an clear code though still slow
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumNum, maxNum = 0, 0

        for num in nums:
            if num:
                sumNum += 1
            else:
                sumNum = 0
            maxNum = max(maxNum, sumNum)

        return maxNum

    # a funny solution with split, even slower!
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        s = ''
        for num in nums:
            s += str(num)

        # can change to the following format
        """
        s = "".join((str(num) for num in nums))
        """


        sps = s.split('0')

        res = 0
        for sp in sps:
            res = max(res, len(sp))

        return res

    # a solution without using max function, fastest so far
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if num:
                count += 1
                if count > res:
                    res = count
            else:
                count = 0
        return res