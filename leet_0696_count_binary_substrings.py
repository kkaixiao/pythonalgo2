"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number
of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011",
"01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive
1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""

class Solution:
    # this solution of O(N^2) failed with Time Limit Exceeded
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        cnt = 0
        for i in range(len(s)):
            for j in range(i+1, len(s), 2):
                if s[i:j+1].count('1') == (j+1-i)//2 and len(set(s[i:j+1][:(j+1-i)//2])) == 1:
                    cnt+=1
        return cnt


    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0

        cnt, cnt1, cnt2 = -1, 0, 0

        prevDigit = None
        for c in s:
            if prevDigit == c:
                cnt1 += 1
                if cnt2 >= cnt1:
                    cnt += 1
            else:
                cnt2 = cnt1
                cnt1 = 1
                cnt += 1
            prevDigit = c
        return cnt