# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# The next number is found by adding up the two numbers before it.
#
# The 2 is found by adding the two numbers before it (1+1)
# The 3 is found by adding the two numbers before it (1+2),
# And the 5 is (2+3),
# and so on!

# we use memoization technique to accelerate computing

def fibonacci(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))