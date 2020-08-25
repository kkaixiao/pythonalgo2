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

        def divisable(strTop, strSub):
            lSub = len(strSub)

            for i in range(int(len(strTop) / lSub)):
                if strTop[i * lSub:(i + 1) * lSub] != strSub:
                    return False

            return True

        l1, l2 = len(str1), len(str2)

        if l1 > l2:
            str1, str2 = str2, str1
            l1, l2 = l2, l1

        res = ""

        for l in range(l1, 1, -1):
            if l1 % l == 0 and l2 % l == 0:

                sub = str1[0:l]
                if divisable(str1, sub) and divisable(str2, sub):
                    return sub

        return res