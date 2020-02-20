def pascal_triangle(n, current_row=0, prev=[]):

    # base case #1, if recursion finishes, the function should return an empty array
    if current_row > n:
        return []
    # start recursion from here, given current_row is by default 0
    elif current_row == 0:
        return pascal_triangle(n, current_row+1, [1])

    # start to do other recursion when current_row goes up, remember, variable prev will be updated after each recursion
    # it is calculated by the calculate_pascal_triangle_row function
    else:
        return [prev] + pascal_triangle(n, current_row+1, calculate_pascal_triangle_row(prev))


# let's calculate items for each recursion
def calculate_pascal_triangle_row(prev):
    res = [1] * (len(prev)+1)
    for i in range(1, len(prev)):
        res[i] = prev[i-1] + prev[i]
    return res


print(pascal_triangle(6))