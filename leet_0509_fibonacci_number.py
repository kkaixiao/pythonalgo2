"""
he Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).



Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Note:

0 ≤ N ≤ 30.
"""

class Solution:
    # recursion version
    def fib_rec(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib_rec(n-1) + self.fib_rec(n-2)

    # iterative version
    def fib_iter(self, n: int) -> int:
        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return a


    def fib_tail(self, n, a=0, b=1):
        if n == 0:
            return a
        if n == 1:
            return b

        return self.fib_tail(n - 1, b, a + b)