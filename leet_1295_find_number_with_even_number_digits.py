'''
Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 10^5

'''

def even_num_and_even_digits(nums):
    count = 0
    for item in nums:
        if len(str(item))%2 == 0:
            count += 1
    return count

def even_num_and_even_digits2(nums):
    odd_count = 0
    for item in nums:
        odd_count += len(str(item))%2

    return len(nums) - odd_count


# this is a one-line version with 'if' statement
def even_num_and_even_digits3(nums):
    return sum(1 for i in nums if not (len(str(i)) % 2))

# this is a one line version without 'if' statement
def even_num_and_even_digits4(nums):

    return sum([not(len(str(i)) % 2) for i in nums])




    # return len(nums) - odd_count

nums1 = [12,345,2,6,7896]
# nums1 = [555,901,482,1771]
print(even_num_and_even_digits4(nums1))