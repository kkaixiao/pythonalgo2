'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''


def plus_one(digits):

    # initiate carry flag to False
    is_carry = False

    # add 1 to the lowest digit, then make a modulus of 10
    digits[len(digits) - 1] = (digits[len(digits) - 1] + 1) % 10

    # if the modulus of 10 to this digit is 0, set the carry flag to True
    if digits[len(digits)-1] % 10 == 0:
        is_carry = True
    else:
        # in this case, we can directly return the result
        return digits

    for i in range(len(digits)-2, -1, -1):
        # if there's a carry flag, we increment the 2nd lowest digit by 1
        if is_carry:
            digits[i] = (digits[i] + 1) % 10

        # we set the carry flag to True, only when current flag is True and modulus of 10 to this digit is 0
        # which means, previous carry flag is True, and current digit is 9
        if digits[i] % 10 == 0 and is_carry:
            is_carry = True
        else:
            # we can then set the carry flag to False and break the for loop
            is_carry = False
            break

    # there's carry flag for the leftmost digit, we can insert a digit of 1 to it
    if is_carry:
        digits.insert(0, 1)
    return digits



my_digits = [9,9,9,5]

print(plus_one(my_digits))