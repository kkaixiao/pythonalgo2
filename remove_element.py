def removeElement(nums, val):
    res = len(nums)

    for each in nums:
        if (each == val):
            res -= 1

    return res


nums = [3,2,2,3]
val = 2
print(removeElement(nums,val))