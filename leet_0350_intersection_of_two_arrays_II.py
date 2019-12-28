

from collections import Counter

# use collections.Counter
def intersect1(nums1, nums2):

    count = Counter(nums1) & Counter(nums2)
    res = []
    for k,v in count.items():
        for i in range(v):
            res.append(k)
    return res



# use own dictionary
def intersect2(nums1, nums2):
    count_dict_1 = {}
    count_dict_2 = {}
    for item in nums1:
        count_dict_1[item] = count_dict_1.get(item, 0) + 1
    for item in nums2:
        count_dict_2[item] = count_dict_2.get(item, 0) + 1
    res = []
    for k1, v1 in count_dict_1.items():
        if count_dict_2.get(k1):
            for i in range(min(v1, count_dict_2.get(k1))):
                res.append(k1)
    return res




# use two pointers
def intersect3(nums1, nums2):
    nums1.sort()
    nums2.sort()
    pointer1 = pointer2 = 0
    res = []
    while (pointer1 < len(nums1)) and (pointer2 < len(nums2)):
        if nums1[pointer1] > nums2[pointer2]:
            pointer2 += 1
        elif nums1[pointer1] < nums2[pointer2]:
            pointer1 += 1
        else:
            res.append(nums1[pointer1])
            pointer1 += 1
            pointer2 += 1
    return res


'''#4: normal method. 84ms'''
# by Ricky Hu
def intersect4(nums1, nums2):
    res = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            res.append(nums1[i])
            nums2.remove(nums1[i])

    return res


# use one dictionary and one list
def intersect5(nums1, nums2):
    count_dict_1 = {}
    list_2 = []
    for item in nums1:
        count_dict_1[item] = count_dict_1.get(item, 0) + 1
    for item in nums2:
        if count_dict_1.get(item):
            list_2.append(item)
            count_dict_1[item] -= 1

    return list_2
    # return res

# arr1, arr2 = [1,2,2,1], [2,2]
arr1, arr2 = [4,9,5], [9,4,9,8,4]
# arr1, arr2 = [3,1,2], [1,1]


print(intersect4(arr1, arr2))

