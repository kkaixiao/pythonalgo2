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
    for i in range(48, 58):
        valid_chars.append(chr(i))

    for i in range(65, 91):
        valid_chars.append(chr(i))

    for i in range(97, 123):
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

#
# for i in range(256):
#     print(i, chr(i))

str1 = "A man, a plan, a canal: Panama"
str1 = "race a car"

print(is_palindrome(str1))