"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make
it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        start, end, count = 0, len(s) - 1, 0

        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                temp, temp1 = s[start + 1:end + 1], s[start:end]
                return temp == temp[::-1] or temp1 == temp1[::-1]

        return True