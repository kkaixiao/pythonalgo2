"""
Given an array arr, replace every element in that array with the greatest element
among the elements to its right, and replace the last element with -1.

After doing so, return the array.



Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""

def replace_elements(ints):
    if len(ints) == 1:
        return [-1]
    res = [-1] * len(ints)
    temp_max = ints[-1]
    for i in range(len(ints) - 2, 0, -1):
        temp_max = max(ints[i + 1], temp_max)

        res[i - 1] = max(ints[i + 1], ints[i])

    res[-2] = ints[-1]
    return res


def replace_elements2(ints):
    last_val = -1
    for val in range(len(ints) - 1, -1, -1):
        ints[val], last_val = last_val, max(ints[val], last_val)
    return ints

arr1 = [17,18,5,4,6,1]
print(replace_elements2(arr1))