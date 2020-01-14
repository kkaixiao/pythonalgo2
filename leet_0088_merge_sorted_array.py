"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted
array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to
hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):

    for i in range(m, m+n):
        print(i, i-n)
        nums1[i] = nums2[i-m]

    nums1.sort()
    print(nums1)


def merge2(nums1, m, nums2, n):

    if n == 0:
        return
    temp = nums1[:]
    idx, idx1, idx2 = 0, 0, 0
    while idx < m + n:

        if idx2 < n and (idx1 >= m or nums2[idx2] < temp[idx1]):
            nums1[idx] = nums2[idx2]
            idx2 += 1
        else:
            nums1[idx] = temp[idx1]
            idx1 += 1
        idx += 1



    print(nums1)

    # for i in range(m, m+n):
    #     print(i, i-n)
    #     nums1[i] = nums2[i-m]
    #
    # nums1.sort()
    # print(nums1)

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3


# nums1 = [1,2,4,5,6,0]
# m = 5
# nums2 = [3]
# n = 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,0,0]
n = 1

merge2(nums1, m, nums2, n)