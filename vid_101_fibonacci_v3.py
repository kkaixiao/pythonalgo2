# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# The next number is found by adding up the two numbers before it.
#
# The 2 is found by adding the two numbers before it (1+1)
# The 3 is found by adding the two numbers before it (1+2),
# And the 5 is (2+3),
# and so on!

# we now use iteration approach to solve this problem


def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


print(fibonacci(10))
