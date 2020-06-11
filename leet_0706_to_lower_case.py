"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string
in lowercase.



Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for c in str:
            if 64 < ord(c) < 91:
                res += chr(ord(c)+32)
            else:
                res += c
        return res