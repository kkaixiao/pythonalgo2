
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


# this is coded by Ricky, super smart and efficient
def relative_sort_array3(arr1, arr2):
    res = []
    for each in arr2:           # iterate all items in arr2
        while (each in arr1):   # as long as the item in arr2 can be found in arr1
            res.append(each)    # add the item to the end of the list to be returned

            arr1.remove(each)  # and immediately remove the item in arr1, therefore in the end of the for loop,
            #                    arr1 will only contains items not found in arr2
    return res+sorted(arr1)


# this is an extremely concise and efficient pythonic code for this question
def relative_sort_array4(arr1, arr2):
    order = {v: i for i, v in enumerate(arr2)}  # create a dictionary to be used for sorting key, or can be called a
    #                                             sorting pattern

    return sorted(arr1, key=lambda a: order.get(a, 1000 + a))   # with the sorting key, arr1 can be ordered by the key

array1 = [2,3,1,3,2,4,6,7,9,2,19]
array2 = [2,1,4,3,9,6]


print(relative_sort_array4(array1, array2))