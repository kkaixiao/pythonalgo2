"""
Given a string, you need to reverse the order of characters in each word within a sentence while
still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space
in the string.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = ''
        word = ''
        for char in s:
            if char != ' ':
                word = char + word
            else:
                sentence += word + ' '
                word = ''
        return sentence + word
