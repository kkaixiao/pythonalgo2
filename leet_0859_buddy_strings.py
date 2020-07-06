"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two
letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Constraints:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        elif A == B:
            return len(set(A)) < len(A)
        else:
            mem = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    mem.append(A[i])
                    mem.append(B[i])

            if len(mem) != 4:
                return False
            else:
                return mem[0]==mem[3] and mem[1]==mem[2]