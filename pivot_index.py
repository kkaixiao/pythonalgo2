
def pivot_index(nums):
    left = 0
    right = sum(nums) - nums[0]
    if left == right:
        return 0
    for i in range(0, len(nums)-1):
        left += nums[i]
        right -= nums[i+1]
        if left == right:
            return i + 1



my_nums = [1, 7, 3, 6, 5, 6]
print(pivot_index(my_nums))