"""
You are given a license key represented as a string S which consists only alphanumeric
character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains
exactly K characters, except for the first group which could be shorter than K, but still
must contain at least one character. Furthermore, there must be a dash inserted between two
groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described
above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except
the first part as it could be shorter as mentioned above.
"""

class Solution:
    # the simplest version
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        tempS = ''
        count = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                tempS = S[i] + tempS
                count += 1
                if count == K:
                    count = 0
                    tempS = '-' + tempS
        if not tempS:
            return ''
        if tempS[0] == '-':
            return tempS[1:].upper()
        else:
            return tempS.upper()

    # the 2nd method
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.split('-')
        S = ''.join(S)

        tempS = ''
        count = 0
        for i in range(len(S)-1, -1, -1):
            tempS = S[i] + tempS
            count += 1
            if count == K:
                count = 0
                tempS = '-' + tempS
        if not tempS:
            return ''
        if tempS[0] == '-':
            return tempS[1:].upper()
        else:
            return tempS.upper()

    # the 3rd version, no big change
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()

        tempS = ''
        count = 0
        for i in range(len(S)-1, -1, -1):
            tempS = S[i] + tempS
            count += 1
            if count == K:
                count = 0
                tempS = '-' + tempS
        if not tempS:
            return ''
        if tempS[0] == '-':
            return tempS[1:]
        else:
            return tempS

    # an improved version, much faster
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        arr = []

        S = S.replace('-', '').upper()

        isolateNumber = len(S) % K

        # isolateNumber is remainder
        # I add this for removing a redundant '-' added
        if isolateNumber != 0:
            arr.append(S[:isolateNumber])

        # a loop end at K
        for i in range(isolateNumber, len(S), K):
            arr.append(S[i: i+K])

        return '-'.join(arr)