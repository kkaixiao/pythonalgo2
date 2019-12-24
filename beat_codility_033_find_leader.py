'''
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of
the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7)
and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A
occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''


# simplest but worst solution
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

# sorting solution
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


# dictionary solution
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

# dominator (with the use of stack)
def leader4(arr):
    if len(arr) <= 2:
        return -1

    stack = []
    for item in arr:
        if len(stack) == 0:
            stack.append(item)
        if item == stack[0]:
            stack.append(item)
        else:
            stack.pop()
    if len(stack) == 0:
        return -1
    else:
        counter = arr.count(stack[0])
        if counter > len(arr)/2:
            return stack[0]



arr1 = [5, 7, 5, 3, 3, 3, 2, 3, 1, 3, 3, 3]
print(leader4(arr1))