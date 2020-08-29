"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".



Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""

class Solution:
    # the replace method
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

    # the split method
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for add in address.split('.'):
            res += add
            res += '[.]'
        return res[:-3]

    # the match '.' index method
    def defangIPaddr(self, address: str) -> str:
        res, curIdx = '', 0
        for i in range(len(address)):
            if address[i] == '.':
                res += address[curIdx: i]
                res += '[.]'
                curIdx = i+1
        res += address[curIdx:]
        return res