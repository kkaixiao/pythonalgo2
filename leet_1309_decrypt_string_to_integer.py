"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English
lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.



Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"


Constraints:

1 <= s.length <= 1000
s[i] only contains digits letters ('0'-'9') and '#' letter.
s will be valid string such that mapping is always possible.
"""


def freq_alphabets(chars):

    res = ''
    idx = 0

    while idx < len(chars)-3:
        if chars[idx + 2] == '#':
            current_item = chars[idx:idx+2]
            idx += 3
        else:
            current_item = chars[idx]
            idx += 1
        res += chr(int(current_item)+96)

    if chars[idx:].find('#') >= 0:
        res += chr(int(chars[-3:-1]) + 96)
    else:
        for char in chars[idx:]:
            res += chr(int(char) + 96)

    return res


# I could not use regular expression correctly, the split function will ignore the last
# portion if there's a number behind
# that is, I can not get the correct answer for:
# str1 =      '12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'
# but not for '12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#3'

import re
def freq_alphabets_regex(chars):
    pattern = re.compile("[1-2][0-9]#")
    seps = pattern.split(chars)
    matched = pattern.findall(chars)
    res = ''
    matched_idx = 0

    for sep in seps:
        if len(sep) > 0:
            for char in sep:
                res += chr(int(char) + 96)
        else:
            res += chr(int(matched[matched_idx][0:2]) + 96)
            matched_idx += 1

    return res


str1 = '12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#3'
# str1 = "10#11#12#"

# print(freq_alphabets(str1))
print(freq_alphabets_regex(str1))