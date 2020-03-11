"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def countPrimes(self, n):
        primes = []
        prime_mark = [0, 0] + [1] * (n - 2)

        for num in range(2, n):
            if prime_mark[num]:
                primes.append(num)
                for j in range(num, n, num):
                    prime_mark[j] = 0
        return len(primes)

sol = Solution()
print(sol.countPrimes(10))