
def equilibrium(arr):
    diffs = []
    for p in range(len(arr)):
        left = sum(arr[:p])
        right = sum(arr[p:])
        diffs.append((p, abs(left-right)))

    # print(diffs)

    lowest_diff = diffs[0][1]
    lowest_index = 0
    # print(lowest)
    for item in diffs:
        if item[1] < lowest_diff:
            lowest_diff = item[1]
            lowest_index = item[0]

    print(lowest_index, lowest_diff)
    return lowest_index




arr1= [3, 1, 2, 4, 3]

print(equilibrium(arr1))