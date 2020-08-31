"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537


Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    # recursion failed on Time Limit Exceeded
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


    # recursion with memoization succeeded
    maps = {}

    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n <= 2:
            return 1

        if n in self.maps:
            return self.maps[n]

        self.maps[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.maps[n]

    # iteration method succeeded
    def tribonacci(self, n: int) -> int:

        a, b, c = 0, 1, 1

        if n == 0:
            return a
        if n <= 2:
            return b

        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
