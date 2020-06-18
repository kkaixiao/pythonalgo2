"""
You're given strings J representing the types of stones that are jewels, and S representing the
stones you have.  Each character in S is a type of stone you have.  You want to know how many of
the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are
case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

class Solution:
    # iterate in S
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for s in S:
            if s in J:
                cnt += 1
        return cnt

    # iterate in J and count occurrences in S
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for j in J:
            cnt += S.count(j)
        return cnt

    # using hash table
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic, cnt = {}, 0

        for j in J:
            dic[j] = 1

        for s in S:
            if s in dic.keys():
                cnt += 1
        return cnt

    # another approach using hash table
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic, cnt = {}, 0

        for s in S:
            dic[s] = dic.get(s, 0) + 1

        for j in J:
            if j in S:
                cnt += dic[j]

        return cnt