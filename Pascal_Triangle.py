
def pascal_triangle(n):
    if n < 0:
        return []

    res = [[1], [1, 1]]

    if n <= 2:
        return res[:n]

    pre_line = res[1]

    for i in range(n-2):

        current_line = pre_line.copy()
        current_line.append(1)

        for j in range(1, i+2):
            current_line[j] = pre_line[j-1] + pre_line[j]

        res.append(current_line)

        pre_line = current_line.copy()

    return res


print(pascal_triangle(1))