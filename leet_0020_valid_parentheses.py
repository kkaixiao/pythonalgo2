"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):

        if len(s)%2 != 0:
            return False

        opening = set('([{')
        matches = set([ ('(', ')'), ('[', ']'), ('{', '}') ])

        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False
        return len(stack) == 0



