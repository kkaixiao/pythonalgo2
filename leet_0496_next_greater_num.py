#Leetcode.num = 496. Next Greater Element I
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
"""


def filter_arr(tuple1):
    nums2, num1 = tuple1
    return [x for x in nums2[1:] if num1 < x]


def next_greater_element(nums1, nums2):
    res = []

    for item in nums1:

        # filtered = [x for x in nums2[nums2.index(item):] if item < x]

        # filtered = list(filter(lambda x: x > item, nums2[nums2.index(item):]))

        filtered = list(map(filter_arr, [(x, item) for x in [nums2[nums2.index(item):]]]))[0]


        if len(filtered) > 0:
            res.append(filtered[0])
        else:
            res.append(-1)

    return res





numsA = [4, 1, 2]
numsB = [1, 3, 4, 2]

nums3 = [2,1,3,5]
nums4 = [2,0,3,1,4,5,7]


print(next_greater_element(numsA, numsB))
