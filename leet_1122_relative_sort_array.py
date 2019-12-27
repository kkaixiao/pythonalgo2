
def relative_sort_array(arr1, arr2):
    sorted_stack = []
    unsorted_stack = []

    for item2 in arr2:
        if item2 in arr1:
            found_indices = [i for i, x in enumerate(arr1) if x == item2]
            for i in found_indices:
                sorted_stack.append(arr1[i])

    for item in arr1:
        if item not in sorted_stack:
            unsorted_stack.append(item)

    return sorted_stack+sorted(unsorted_stack)


def relative_sort_array2(arr1, arr2):
    sorted_stack = []
    unsorted_stack =[]

    for item2 in arr2:
        found_indices = [i for i, x in enumerate(arr1) if x == item2]
        found_stack = [y for i, y in enumerate(arr1) if i in found_indices]
        sorted_stack.extend(found_stack)

    for item in arr1:
        if item not in sorted_stack:
            unsorted_stack.append(item)

    return sorted_stack+sorted(unsorted_stack)


array1 = [2,3,1,3,2,4,6,7,9,2,19]
array2 = [2,1,4,3,9,6]


print(relative_sort_array2(array1, array2))