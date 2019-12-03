
def equilibrium(arr):

    sum_left = arr[0]
    sum_right = sum(arr) - arr[0]

    diff = abs(sum_left - sum_right)
    p = 0

    for i in range(1, len(arr)):
        sum_left += arr[i]
        sum_right -= arr[i]

        curr_diff = abs(sum_left - sum_right)

        if diff > curr_diff:
            diff = curr_diff
            p = i

    return diff, p+1



    # return p

    # while curr_diff > pre_diff:









arr1= [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

# arr1= [3, 1, 2, 4, 3]
# print(abs(sum(arr1[:5]) - sum(arr1[5:])))

print(equilibrium(arr1))