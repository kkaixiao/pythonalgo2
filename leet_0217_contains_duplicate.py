
def contains_duplicate(nums):
    if len(nums) < 2:
        return False
    stack = []
    nums.sort()

    for i in range(len(nums) - 1):
        stack.append(nums[i])
        if nums[i+1] == stack[0]:
            return True
        else:
            stack.pop()

    return False


def contains_duplicate2(nums):

    dict_nums = {}
    for item in nums:
        if dict_nums.get(item):
            dict_nums[item] += 1
        else:
            dict_nums[item] = 1

    for k,v in dict_nums.items():
        if v > 1:
            return True

    return False


def contains_duplicate3(nums):
    if len(nums) > len(set(nums)):
        return True
    else:
        return False


from collections import Counter
def contains_duplicate4(nums):
    for k, v in Counter(nums).items():
        if v > 1:
            return True
    return False


def contains_duplicate5(nums):

    dict_nums = {}
    for item in nums:
        dict_nums[item] = dict_nums.get(item, 0) + 1

    for k,v in dict_nums.items():
        if v > 1:
            return True

    return False


def contains_duplicate6(nums):

    dict_nums = {x: nums.count(x) for x in nums}

    for k, v in dict_nums.items():
        if v > 1:
            return True

    return False

arr1 = [1,2,3,4]
arr2 = [1,2,3,1]

print(contains_duplicate(arr2))
