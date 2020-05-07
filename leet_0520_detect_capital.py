"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution:
    # the first simple but slow solution
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        condition1 = condition2 = condition3 = False

        if word[0] == word[0].lower():
            condition2 = True
        else:
            if word[1] == word[1].upper():
                condition1 = True
            else:
                condition3 = True

        if condition2:
            for i in range(1, len(word)):
                if word[i] == word[i].upper():
                    return False
            return True
        elif condition3:
            for i in range(2, len(word)):
                if word[i] == word[i].upper():
                    return False
            return True
        elif condition1:
            for i in range(2, len(word)):
                if word[i] == word[i].lower():
                    return False
            return True

    # solution 2
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True

        if word[0] == word[0].lower() and word[1] == word[1].upper():
            return False

        condition1 = condition2 = condition3 = False

        if word[0] == word[0].upper() and word[1] == word[1].upper():
            condition1 = True
        if word[0] == word[0].lower() and word[1] == word[1].lower():
            condition2 = True
        if word[0] == word[0].upper() and word[1] == word[1].lower():
            condition3 = True

        if condition1:
            for i in range(2, len(word)):
                if word[i] == word[i].lower():
                    return False
        if condition2:
            for i in range(2, len(word)):
                if word[i] == word[i].upper():
                    return False
        if condition3:
            for i in range(2, len(word)):
                if word[i] == word[i].upper():
                    return False
        return True

    # embedded function
    def detectCapitalUse(self, word):

        def condition1(word):
            if word.isupper():
                return True

        def condition2(word):
            if word.islower():
                return True

        def condition3(word):
            if word[0].isupper() and word[1:].islower():
                return True

        if condition1(word) or condition2(word) or condition3(word):
            return True
        else:
            return False

    # embedded function


    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        if (word[0].islower()):
            for a in range(1, len(word)):
                if (word[a].isupper()):
                    return False
        else:
            onlyLower = True if word[1].islower() else False

            for a in range(2, len(word)):
                if (onlyLower and word[a].isupper()) or (not onlyLower and word[a].islower()):
                    return False

        return True