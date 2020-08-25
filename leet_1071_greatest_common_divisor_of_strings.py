"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with
itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def isGCD(strA, strB):

            times, patlen = len(strA) // len(strB), len(strB)
            for i in range(times):
                if strA[i * patlen:i * patlen + patlen] != strB:
                    return False
            return True

        l1, l2 = len(str1), len(str2)
        if len(str1) < len(str2):
            str1, str2 = str2, str1
            l1, l2 = l2, l1

        for i in range(l2 - 1, -1, -1):
            compareStr = str2[:i + 1]

            if l1 % len(compareStr) == 0 and l2 % len(compareStr) == 0:
                if isGCD(str1, compareStr) and isGCD(str2, compareStr):
                    return compareStr
        return ''