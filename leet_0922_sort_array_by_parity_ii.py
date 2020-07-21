"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the
integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""


class Solution:
    # solution 1, the worst one
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even, res = [], [], []
        for i in range(len(A)):
            if A[i] % 2:
                odd.append(A[i])
            else:
                even.append(A[i])
        for k in range(len(odd)):
            res.append(even[k])
            res.append(odd[k])

        return res

    # a faster solution
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res, evenIdx, oddIdx = [0] * len(A), 0, 1

        for i in A:
            if not i % 2:
                res[evenIdx] = i
                evenIdx += 2

            else:
                res[oddIdx] = i
                oddIdx += 2

        return res