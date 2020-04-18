"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row
must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        for i in range(int(math.sqrt(n)), n//2+3):
            if (i * (i-1))/2 >= n:
                return i-1 - math.ceil(((i * (i-1))/2 - n)/n)

    # my old version, the prior one was evolved from the following one
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        for i in range(int(math.sqrt(n)), n//2+3):
            if (i * (i-1))/2 == n:
                return i-1
            elif (i * (i-1))/2 > n:
                return i - 2


    # the third with binary search, can beat 97%

    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return 0

        start, end = int(math.sqrt(n)), n // 2 + 2
        mid = (start + end) // 2

        while start <= end:
            if mid * (mid + 1) // 2 > n:
                end = mid - 1
                mid = (start + end) // 2
            elif mid * (mid + 1) // 2 < n:
                start = mid + 1
                mid = (start + end) // 2
            else:
                return mid

        return mid

