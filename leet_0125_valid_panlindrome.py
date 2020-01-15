"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""
# 48=0, 57= 9, 65=A, 90=Z, 97=a, 122=z

def is_palindrome(chars):

    if len(chars) == 1 or len(chars) == 0:
        return True

    valid_chars = []
    for i in range(48, 58):  # numbers
        valid_chars.append(chr(i))

    for i in range(65, 91):  # upper case chars
        valid_chars.append(chr(i))

    for i in range(97, 123):  # lower case chars
        valid_chars.append(chr(i))

    processed_chars = ''
    for char in chars:
        if char in valid_chars:
            processed_chars += char

    processed_chars = processed_chars.lower()

    len_processed_chars = len(processed_chars)

    for i in range(len_processed_chars//2):
        if processed_chars[i] != processed_chars[len_processed_chars-i-1]:
            return False

    return True


def is_palindrome2(chars):

    if len(chars) == 1 or len(chars) == 0:
        return True

    alpha_numeric_removed_chars = filter(lambda x: (ord(x) in range(65, 91)) or (ord(x) in range(48, 58)) or (ord(x) in range(97, 122)), chars)

    processed_chars = list(map(lambda x: chr(ord(x) - 32) if ord(x) in range(97, 123) else x, alpha_numeric_removed_chars))

    for i in range(len(processed_chars)//2):
        if processed_chars[i] != processed_chars[len(processed_chars)-i-1]:
            return False

    return True

#
# for i in range(256):
#     print(i, chr(i))

str1 = "A man, a plan, a canal: Panama"
# str1 = "race a car"

print(is_palindrome2(str1))