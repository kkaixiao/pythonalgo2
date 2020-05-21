"""
We define a harmounious array as an array where the difference between its maximum value and
its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence
among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].


Note: The length of the input array will not exceed 20,000.
"""


class Solution:
    # first version but has redundant processing
    def findLHS(self, nums: List[int]) -> int:
        numDict = {}
        nums.sort()

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1

        listNum = list(numDict)

        idxList = []
        for i in range(0, len(listNum) - 1):

            if listNum[i] - listNum[i + 1] == -1:
                idxList.append((listNum[i], listNum[i + 1]))

        res = []
        if len(idxList) == 0:
            return 0
        for idxItem in idxList:
            res.append(numDict[idxItem[0]] + numDict[idxItem[1]])

        return max(res)

    # second improved version
    def findLHS(self, nums: List[int]) -> int:
        numDict = {}
        nums.sort()

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1

        listNum = list(numDict)

        subSumList = []
        for i in range(0, len(listNum) - 1):

            if listNum[i + 1] - listNum[i] == 1:
                subSumList.append(numDict[listNum[i]] + numDict[listNum[i + 1]])

        return 0 if len(subSumList) == 0 else max(subSumList)

    # third improved version
    def findLHS(self, nums: List[int]) -> int:
        numDict = {}

        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1

        maxNum = 0
        for oneKey in numDict.keys():
            if oneKey+1 in numDict.keys():
                maxNum = max(maxNum, numDict[oneKey]+numDict[oneKey+1])

        return maxNum