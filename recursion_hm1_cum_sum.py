
def cum_sum(n):
    if n == 0:
        return n
    return n + cum_sum(n-1)

print(cum_sum(2))