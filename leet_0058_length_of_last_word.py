'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return
the length of last word (last word means the last appearing word if we loop from left to right)
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


def length_of_last_word(chars):
    last_word_end, last_word_start = -1, -1
    for i in range(len(chars)-1, -1, -1):
        if last_word_end == -1 and chars[i] != ' ':
            last_word_end = i
        elif last_word_start == -1 and chars[i] == ' ' and last_word_end != -1:
            last_word_start = i
        elif last_word_start > -1 and last_word_start > -1:
            break
    return len(chars[last_word_start+1:last_word_end+1])


def length_of_last_word2(chars):
    last_word_end, last_word_start = -1, -1
    idx = len(chars) - 1
    while (last_word_start == -1 or last_word_end == -1) and idx > -1:
        if last_word_end == -1 and chars[idx] != ' ':
            last_word_end = idx
        elif last_word_start == -1 and chars[idx] == ' ' and last_word_end != -1:
            last_word_start = idx
        idx -= 1

    return len(chars[last_word_start+1:last_word_end+1])

# str1 = "Hello World "
str1 = 'ba '
# str1 = ' b  '
# str1 = ' '
# str1 = ''
print(length_of_last_word2(str1))