"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a
prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in
binary. For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)

Example 1:

Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
Example 2:

Input: L = 10, R = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
Note:

L, R will be integers L <= R in the range [1, 10^6].
R - L will be at most 10000.
"""


class Solution:
    # much faster approach
    def countPrimeSetBits(self, L, R):

        # given L, R will be integers L <= R in the range [1, 10^6],
        # the maximum that any number of '1' will be 19, as can be found:
        # print(len(bin(10**6))-2)

        primeNums = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0
        for n in range(L, R + 1):
            if bin(n)[2:].count('1') in primeNums:
                res += 1

        return res

    # normal approach, not fast enough
    def countPrimeSetBits(self, L, R):
        def isPrime(num):
            if num in [1,4,6,8,9,10,12]:
                return False
            if num in [2,3,5,7,11,13]:
                return True
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

        res = 0

        for j in range(L, R + 1):
            if isPrime(bin(j)[2:].count('1')):
                res += 1
        return res