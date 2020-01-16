"""
1189. Maximum Number of Balloons
Easy

134

19

Add to List

Share
Given a string text, you want to use the characters of text to form as many instances of
the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that
can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2


Example 3:
Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""

def maxNumberOfBalloons(text, balloon_str='balloon'):
    balloon_list_check = list(balloon_str)
    count = 0

    for _, char in enumerate(text):

        if char in balloon_list_check:
            balloon_list_check.remove(char)

            if len(balloon_list_check) == 0:
                count += 1
                balloon_list_check = list(balloon_str)

    return count


def max_number_of_balloons(text_list, balloon_str='balloon', count=0):
    if len(text_list) < len(balloon_str):
        return count

    balloon_list_check = list(balloon_str)

    for _, char in enumerate(balloon_str):
        balloon_list_check.remove(char)
        if char in text_list:
            text_list.remove(char)

            if len(balloon_list_check) == 0:
                return max_number_of_balloons(text_list, 'balloon', count+1)


def clean_string(text, balloon_str='balloon'):
    balloon_list = balloon_str
    text_list = list(text)
    for char in text_list:
        if char not in balloon_list:
            text_list.remove(char)
    return ''.join(text_list)


print(maxNumberOfBalloons('loonbalxballpoonballtdoo'))