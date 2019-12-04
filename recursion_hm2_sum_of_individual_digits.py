
def sum_individual_digits(n):
    if n < 10:
        return n

    return n % 10 + sum_individual_digits(int(n/10))




print(sum_individual_digits(12340))
