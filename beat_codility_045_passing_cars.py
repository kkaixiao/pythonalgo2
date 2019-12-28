
def passing_cars(nums):  # use suffix sum method

    car_stack = []
    one_sum = 0
    for i in range(len(nums)-1, -1, -1):
        one_sum += nums[i]
        if nums[i] == 0:
            car_stack.append(one_sum)

    return sum(car_stack)


def passing_cars2(nums):  # use prefix sum method designed by the tutor
    suffix_sum = [0] * (len(nums)+1)

    count = 0

    for i in range(len(nums)-1, -1, -1):
        suffix_sum[i] = nums[i] + suffix_sum[i+1]

        if nums[i] == 0:
            count += suffix_sum[i]
        if count > 1000000000:
            return -1

    return count



arr1 = [0, 1, 0, 1, 1]

print(passing_cars2(arr1))