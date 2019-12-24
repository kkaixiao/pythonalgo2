
def leader(arr):
    if len(arr) <= 2:
        return -1
    set_arr = set(arr)
    for item_set in set_arr:
        count = 0
        for item_arr in arr:
            if item_arr == item_set:
                count += 1
        if count > len(arr)/2:
            return item_set
    return -1

arr1 = [2, 3, 2]
print(leader(arr1))