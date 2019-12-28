
# the first method using linear array assignment
# the complexity should be O(N)

def move_zeros(nums):

    non_zero_count = 0
    for item in nums:
        if item != 0:
            nums[non_zero_count] = item
            non_zero_count += 1
    for i in range(non_zero_count, len(nums)):
        nums[i] = 0




arr1 = [0, 1, 0, 3, 12]
print(move_zeros(arr1))