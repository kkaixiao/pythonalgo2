

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


# nums1, nums2 = [1,2,2,1], [2,2]
nums1, nums2 = [4,9,5], [9,4,9,8,4]
# nums1, nums2 = [3,1,2], [1,1]


print(intersect2(nums1, nums2))

