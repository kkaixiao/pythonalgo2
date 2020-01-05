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

    for i in range(0, len(char_num_list)):
        if (char_num_list[i] - (sum(char_num_list[i+1:]) + sum(char_num_list[:i]))) > 1:
            return ''

    res = ''
    count = 0
    for k, v in char_dict.items():
        count += v

    #
    # import operator
    # sorted_char_dict = dict(sorted(char_dict.items(), reverse=True, key=operator.itemgetter(1)))

    res_arr = [None]*count

    count_ndx = 0
    for k, v in char_dict.items():

        for i in range(v):
            pos = (count_ndx * 2) % count
            res_arr[pos] = k
            count_ndx += 1



    return ''.join(res_arr)

str1 = 'bfrbs'
str2 = 'aab'
str3 = 'lllvo'
str4 = 'aaabbbcccd'
str5 = 'abbabbaaab'

print('result is', reorganizeString(str5))