"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key
might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your
friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pName, pTyped = 0, 0

        while pName < len(name) and pTyped < len(typed):
            if name[pName] != typed[pTyped]:
                return False
            cntName, cName, cntTyped, cType = 0, name[pName], 0, typed[pTyped]

            while pName < len(name) and name[pName] == cName:
                cntName += 1
                pName += 1

            while pTyped < len(typed) and typed[pTyped] == cType:
                cntTyped += 1
                pTyped += 1

            if cntName > cntTyped:
                return False

        if pName == len(name) and pTyped == len(typed):
            return True

        return False