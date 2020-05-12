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

    # pythonic stuff added
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = ''
        for word in words:
            res += word[::-1] + ' '
        return res[:-1]

    # some pythonic stuff removed
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        res = ''
        for word in words:
            temp = ''
            for char in word:
                temp = char + temp
            res += temp + ' '

        return res[:-1]