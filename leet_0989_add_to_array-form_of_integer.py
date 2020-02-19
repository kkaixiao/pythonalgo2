"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right
order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
"""

class Solution:
    def addToArrayForm(self, A, K):
        len_A = len(A)
        num_A = 0
        for i in range(len_A):
            num_A += A[i] * 10**(len_A - i - 1)

        str_sum = str(num_A + K)
        res = []
        for char in str_sum:
            res.append(int(char))

        return res

    def addToArrayForm2(self, A, K):
        idx = len(A) - 1
        A[idx] += K
        while A[idx] >= 10:
            a = ((A[idx] // 10) * 10)
            A[idx] -= a
            idx -= 1
            if idx < 0:
                A = [a // 10] + A
                idx = 0
            else:
                A[idx] += a // 10

        return A

sol = Solution()
sol.addToArrayForm([2,7,4], 181)
