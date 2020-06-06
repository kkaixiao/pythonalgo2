"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits
will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""


class Solution:
    # use bin function to compare values
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 2:
            return True
        binVal = bin(n)[2:]
        preChar = binVal[0]
        for i in range(1, len(binVal)):
            if preChar == binVal[i]:
                return False
            preChar = binVal[i]

        return True

    # with pow function to match value
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 2:
            return True

        val = 1
        t = 1
        while (val < n):
            val += pow(4, t)
            if (val == n):
                return True
            t += 1

        val = 2
        t = 1
        while (val < n):
            val += pow(4, t) * 2
            if (val == n):
                return True
            t += 1
        return False