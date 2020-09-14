"""
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its
decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can
return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal
representation.
Example 2:

Input: n = 11
Output: [2,9]
Example 3:

Input: n = 10000
Output: [1,9999]
Example 4:

Input: n = 69
Output: [1,68]
Example 5:

Input: n = 1010
Output: [11,999]
"""


class Solution:
    # method one, looks slow
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def checkNonZero(num):
            for c in str(num):
                if c == '0':
                    return False
            return True

        for i in range(n // 2 + 1):
            if checkNonZero(i) and checkNonZero(n - i):
                return [i, n - i]

    # a faster approach by iterating on number digit, instead of on number
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n < 10:
            return [1, n - 1]

        digits = math.floor(math.log10(n)) + 1  # get digit number
        a = 10 ** (digits - 1) - 1  # assign a to be all '9' digits
        b = n - a
        b2 = b  # set b to be n-a

        # iteratively checking digits in b
        for i in range(digits - 1):
            dLast = b2 % 10
            if not dLast:
                a -= 10 ** i
                b += 10 ** i
            b2 = (b2 - dLast) // 10

        return [a, b]