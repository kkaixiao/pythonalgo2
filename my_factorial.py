
def factorial(n):
    if n == 0:
        return 1

    return n*factorial(n-1)

# n! = n*(n-1)!
# n! = n*(n-1)*(n-2)!
# n! = n*(n-1)*(n-2)*(n-3)!

print(factorial(3))