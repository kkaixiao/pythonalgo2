'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not
the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''


def reorganizeString(S):
    arr = list(S)
    arr.sort(reverse=True)
    char_dict = {}
    for i in range(len(arr)):
        if char_dict.get(arr[i]):
            char_dict[arr[i]] += 1
        else:
            char_dict[arr[i]] = 1

    char_num_list = list(char_dict.values())

    pre_value = char_num_list[0]
    for i in range(1, len(char_num_list)):
        if (pre_value - (sum(char_num_list[i:]) + sum(char_num_list[:i-1]))) > 1:
            return ''
        pre_value = char_num_list[i]

    res = ''
    count = 0
    for k, v in char_dict.items():
        count += v

    import operator
    sorted_char_dict = dict(sorted(char_dict.items(), reverse=True, key=operator.itemgetter(1)))

    while count > 0:
        for k, v in sorted_char_dict.items():
            if v > 0:
                res += k
                sorted_char_dict[k] -= 1
            count -= 1
    return res

str1 = 'abbbbcc'
str2 = 'aaabbbcccd'

print('result is', reorganizeString(str1))