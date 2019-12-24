
def leader1(arr):
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

def leader2(arr):
    if len(arr) <= 2:
        return -1
    arr.sort()
    mid_val = arr[int(len(arr)/2)]
    count = 0
    first_idx = arr.index(mid_val)
    for i in range(first_idx, len(arr)):
        if arr[i] != mid_val:
            if count > len(arr)/2:
                return mid_val
            else:
                return -1
        count += 1

    return mid_val if count > len(arr)/2 else -1

def leader3(arr):
    if len(arr) <= 2:
        return -1
    dict = {}
    for item in arr:
        if dict.get(item) is None:
            dict[item] = 1
        else:
            dict[item] += 1
    leader = 0
    leader_num = 0
    for k, v in dict.items():
        if v > leader:
            leader = v
            leader_num = k
    return leader_num if leader > len(arr)/2 else -1



arr1 = [2, 3, 2, 3]
print(leader3(arr1))