"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution(object):
    # one function, O(n^2), passed but very slow
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s

        def isPalindrome(sub):
            if sub == sub[::-1]:
                return True

        for l in range(len(s), -1, -1):
            for head in range(len(s) - l):
                tail = head + l + 1
                if isPalindrome(s[head: tail]):
                    return s[head: tail]


    # Very fast solution, beats 98%.
    def longestPalindrome(self, s: str) -> str:
        """
        This solution is similar to O(n^3) bruteforce, but uses approach that we doesn't need to check
        substrings shorter than current max_palindrom. On each iteration we enough to check only two
        substrings: [i - len(max_palindrom) - 1 : i + 1] and [i - len(max_palindrom) : i + 1]. Thus it
        has O(n^2) time complexity.
        """
        max_palindrome = ''
        for i in range(0, len(s)):
            # we will need to check substrings, that are longer than max_palindrome
            start = i - len(max_palindrome) - 1
            if start < 0:
                # if start < 0 then current max_palindrome == s[0 : i]
                # thus, we only need to check substring that 1 char longer
                candidate = s[:i + 1]
                if candidate == candidate[::-1]:
                    max_palindrome = candidate
                    continue
            else:
                # check substring that 2 chars longer than current max_palindrom
                candidate = s[start: i + 1]
                if candidate == candidate[::-1]:
                    max_palindrome = candidate
                    continue

                # check substring that 1 char longer than current max_palindrom
                candidate = candidate[1:]
                if candidate == candidate[::-1]:
                    max_palindrome = candidate
                    continue

        return max_palindrome