# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# The next number is found by adding up the two numbers before it.
#
# The 2 is found by adding the two numbers before it (1+1)
# The 3 is found by adding the two numbers before it (1+2),
# And the 5 is (2+3),
# and so on!

# we use memoization technique to accelerate computing.

# cache, consider setting n to a number bigger than function call input n

# the ordinary memoization
n = 100
cache = [None] * (n+1)


def fibonacci(n):

    # base case
    if n <= 0:
        return 0
    elif n <= 2:
        return 1

    # check cache

    if cache[n]:
        return cache[n]

    # keep setting cache
    # cache.append(fibonacci(n-1) + fibonacci(n-2))
    cache[n] = fibonacci(n-1) + fibonacci(n-2)

    return cache[n]


# print(fibonacci(50))

## end of the ordinary memoization


from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cache_built_in(n):
    if n < 2:  # base case
        return n
    return fib_cache_built_in(n-1) + fib_cache_built_in(n-2)


print(fib_cache_built_in(10))