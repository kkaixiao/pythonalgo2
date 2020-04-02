"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        idxs = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                idxs.append(i)

        for i in range(len(idxs)//2):
            s[idxs[i]], s[idxs[-i-1]] = s[idxs[-i-1]], s[idxs[i]]

        return ''.join(s)

    def reverseVowels_one_loop(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        start, end = 0, len(s)-1
        s = list(s)
        while start < end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in vowels:
                end -= 1
            elif s[end] in vowels:
                start += 1
            else:
                start += 1
                end -= 1
        return ''.join(s)

sol = Solution()
s = 'hello'
print(sol.reverseVowels(s))