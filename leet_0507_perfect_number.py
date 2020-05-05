"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive
divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false
when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""


class Solution:
    # first, but over time version
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divisors = [1]
        for i in range(2, num//2+1):
            if num % i == 0:
                divisors.append(i)

        return sum(divisors) == num

    # same version, but without using list
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sumFactors = 1
        for i in range(2, num//2+1):
            if num % i == 0:
                sumFactors += i

        return sumFactors == num

    # second, much faster
    def checkPerfectNumber(self, num: int) -> bool:

        def checkPerfectNumber(self, num: int) -> bool:

            if num <= 1:
                return False

            sumFactors = 1

            for i in range(2, ceil(math.sqrt(num))):
                if num % i == 0:
                    if i == num // i:
                        sumFactors += i

                    else:
                        sumFactors += (i + num // i)

            return sumFactors == num