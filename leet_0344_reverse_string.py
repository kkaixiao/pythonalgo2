"""
Write a function that reverses a string. The input string is given as an array of characters
char[].

Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # this version is very slow
        for i in range(len(s)-2, -1, -1):
            s.append(s[i])
            s.pop(i)

    def reverseString_2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]


    def reverseString_3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #pythonic version
        s[0:] = s[::-1]

