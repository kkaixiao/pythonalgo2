"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
"""

def ugly_number(num):
    if num > 2**31-1 or num < -(2*31) or num == 0:
        return False
    if num == 1:
        return True
    while num != 1:
        ugly_result = ugly_dividable(num)
        if ugly_result > 1:
            num //= ugly_result
        else:
            return False

    return True


def ugly_dividable(num):
    ugly_primes = [2, 3, 5]
    for item in ugly_primes:
        if num % item == 0:
            return item
    return -1


def ugly_dividable_rec(num):
    ugly_primes = [2, 3, 5]
    for item in ugly_primes:
        if num % item == 0:
            return num//item
    return 0


def ugly_number_rec(num):
    if num > 2**31-1 or num < -(2*31) or num == 0:
        return False
    elif num == 1:
        return True
    else:
        test_num = ugly_dividable_rec(num)
        if test_num == 0:
            return False
        else:
            return ugly_number_rec(test_num)

# the following functions are made of double (enclosed) recursion functions
def ugly_dividable_rec2(num):
    if num == 1 or num == 0:
        return num
    ugly_primes = [2, 3, 5]

    idx = 0
    while idx < len(ugly_primes):
        print(num)
        if num % ugly_primes[idx] == 0:
            return ugly_dividable_rec2(num//ugly_primes[idx])
        else:
            idx += 1
    return 0



def ugly_number_rec2(num):
    if num > 2**31-1 or num < -(2*31) or num == 0:
        return False
    elif num == 1:
        return True
    else:
        test_num = ugly_dividable_rec2(num)
        if test_num == 0:
            return False
        else:
            return ugly_number_rec2(test_num)



# print(ugly_dividable(11))


# print(ugly_number(6))

print(ugly_number_rec2(6))


