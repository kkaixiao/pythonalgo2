
def equilibrium(arr):

    p = 1
    left = sum(arr[:p])
    right = sum(arr[p:])

    pre_diff = abs(right - left)
    curr_diff = pre_diff
    while curr_diff <= pre_diff:
        pre_diff = curr_diff
        p += 1
        left = sum(arr[:p])
        right = sum(arr[p:])
        curr_diff = abs(right - left)
        # print(p)



    return p -1

    # while curr_diff > pre_diff:









# arr1= [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

arr1= [8, 2, 3, 1, 2, 3, 3, 1, 2, 4, 3]
print(abs(sum(arr1[:5]) - sum(arr1[5:])))

print(equilibrium(arr1))