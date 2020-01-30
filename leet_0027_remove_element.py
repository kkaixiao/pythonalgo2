def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


def removeElement2(nums, val):
    not_repeated_index_list = []
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            not_repeated_index_list.append(nums[i])
            count += 1

    for j in range(count):
        nums[j] = not_repeated_index_list[j]

    return count

nums = [3,2,2,3]
val = 2
print(removeElement(nums,val))