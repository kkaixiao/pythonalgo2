"""
Write a function that calculates the GCD (Greatest Common Divisor) of two numbers recursively.

Examples
gcd(10, 20) ➞ 10

gcd(1, 3) ➞ 1

gcd(5, 7) ➞ 1

gcd(2, 6) ➞ 2
"""


def gcd(num_small, num_big, divisor):
    if num_small % divisor == 0 and num_big % divisor == 0:
        return divisor
    else:
        return gcd(num_small, num_big, divisor-1)


num1 = 80
num2 = 1900

if num1 > num2:
    num1, num2 = num2, num1

print(gcd(num1, num2, num1))