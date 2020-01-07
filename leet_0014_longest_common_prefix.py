"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


def longest_common_prefix(strs):
    if len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]

    min_chars_size = len(strs[0])
    for chars in strs[1:]:
        min_chars_size = min(min_chars_size, len(chars))

    idx = 0

    while idx < min_chars_size:
        temp_char = strs[0][idx]
        for chars in strs[1:]:
            if chars[idx] != temp_char:
                return strs[0][:idx]

        idx += 1

    return strs[0][:idx]




strs1 = ["flower", "flow", "flight"]
# strs1 = ["c", "c"]
print(longest_common_prefix(strs1))