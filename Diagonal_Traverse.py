def diagonal_traverse(two_d_array):
    if not two_d_array or len(two_d_array) == 0:
        return []

    output = [two_d_array[0][0]]

    row_num, col_num = len(two_d_array), len(two_d_array[0])

    row_index, col_index = 0, 0

    while 0 <= row_index < row_num and 0 <= col_index < col_num:
        if col_index < col_num-1:
            col_index += 1
        else:
            row_index += 1

        while 0 <= row_index < row_num and 0 <= col_index < col_num:
            output.append(two_d_array[row_index][col_index])
            row_index, col_index = row_index + 1, col_index - 1
        row_index, col_index = row_index - 1, col_index + 1

        if row_index < row_num-1:
            row_index += 1
        else:
            col_index += 1

        while 0 <= row_index < row_num and 0 <= col_index < col_num:
            output.append(two_d_array[row_index][col_index])
            row_index, col_index = row_index - 1, col_index + 1

        row_index, col_index = row_index + 1, col_index - 1

    return output

input = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(diagonal_traverse(input))