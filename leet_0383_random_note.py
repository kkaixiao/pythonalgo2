"""
Given an arbitrary ransom note string and another string containing letters from all the
magazines, write a function that will return true if the ransom note can be constructed from
the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    # convert to list and process
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote, magazine = list(ransomNote), list(magazine)
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                magazine.pop(magazine.index(char))

        return True

    # direct string operation
    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                magazine = magazine.replace(char,'', 1)

        return True

    # set comparison
    def canConstruct_3(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteSet = set(ransomNote)
        for char in ransomNoteSet:
            if ransomNote.count(char) > magazine.count(char):
                return False

        return True

    # dictionary operation
    def canConstruct_4(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDict = {}
        magazineDict = {}
        for char in ransomNote:
            ransomNoteDict[char] = ransomNoteDict.get(char, 0) + 1

        for char in magazine:
            magazineDict[char] = magazineDict.get(char, 0) + 1

        for char in ransomNoteDict:
            if char in magazineDict and magazineDict[char] >= ransomNoteDict[char]:
                continue
            else:
                return False

        return True