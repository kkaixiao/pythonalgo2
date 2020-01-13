"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part
of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during
an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is
consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    if len(needle) == 0:
        return 0

    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i

    return -1


def strStr2(haystack, needle):
    if len(needle) == 0:
        return 0

    return haystack.find(needle)


def strStr_kmp(haystack, needle):

    m = len(haystack)
    n = len(needle)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * n
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    compute_lps_array(needle, n, lps)
    print(lps)

    i = 0  # index for txt[]
    while i < m:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == n:
            # print("Found pattern at index " + str(i - j))
            return i - j
            # j = lps[j - 1]

            # mismatch after j matches
        elif i < m and needle[j] != haystack[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps_array(needle, n, lps):
    len_long_prev_suffix = 0  # length of the previous longest prefix suffix

    lps[0] = 0  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < n:
        if needle[i] == needle[len_long_prev_suffix]:
            len_long_prev_suffix += 1
            lps[i] = len_long_prev_suffix
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len_long_prev_suffix != 0:
                len_long_prev_suffix = lps[len_long_prev_suffix - 1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

"""
def create_pattern_string(pat):
    pat_match_indices = [0] * len(pat)

    gap = 1
    for current_index in range(1, len(pat)):
        # print(current_index, gap, current_index - gap)

        # if the current value == prefix, we should set match array as 1
        if pat[current_index] == pat[current_index - gap]:
            pat_match_indices[current_index] = pat_match_indices[current_index-1] + 1
            # ABCDABCABCABABCABCD
        else:
            gap = current_index
            if pat[current_index] == pat[0]:
                pat_match_indices[current_index] = 1

    return pat_match_indices
"""


def create_pattern_string2(pat):
    pat_match_indices = [0] * len(pat)

    tail = 0
    head = 1

    while head < len(pat):

        if pat[head] == pat[tail]:
            pat_match_indices[head] = tail + 1
            tail += 1
        else:
            while pat[head] != pat[tail] and tail > 0:
                tail = pat_match_indices[tail - 1]
                if pat[head] == pat[tail]:
                    pat_match_indices[head] = tail+1
                    tail += 1
                    break
        head += 1

    return pat_match_indices



def strStr_kmp2(haystack, needle):
    if len(needle) < 1:
        return -1
    if len(needle) == 1:
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return i
        return -1

    pat_indices = create_pattern_string2(needle)
    print(pat_indices)

    index_haystack = index_needle = 0

    while index_haystack < len(haystack) and index_needle < len(needle):
        if haystack[index_haystack] == needle[index_needle]:
            if index_needle == len(needle) - 1:
                return index_haystack - index_needle
            # print(index_needle, index_haystack)
            index_needle += 1
            index_haystack += 1
        else:
            while index_needle >= 0 and index_haystack < len(haystack):
                if index_needle != 0:
                    index_needle = pat_indices[index_needle - 1]
                else:
                    index_needle = pat_indices[index_needle]

                if haystack[index_haystack] == needle[index_needle]:
                    index_haystack += 1
                    index_needle += 1
                    break
                else:
                    index_haystack += 1


    return -1


def strStr_kmp3(haystack, needle):
    if len(needle) < 1:
        return -1

    if len(needle) == 1:
        for i in range(len(haystack)):
            if haystack[i] == needle:
                return i
        return -1

    i = 0  # index for haystack
    j = 0  # index for needle
    len_haystack = len(haystack)
    len_needle = len(needle)

    pat_indices = create_pattern_string2(needle)

    while i < len_haystack:

        if needle[j] == haystack[i]:  # found one char matches, increment both i and j
            i += 1
            j += 1

        if j == len_needle:   # found all chars match, return the index: i - j
            return i - j
        elif i < len_haystack and haystack[i] != needle[j]:   # if not match and haystack has not been iterated
            if j != 0:  # if needle is not at the top (always 0), find the previous index which shows the starting point
                j = pat_indices[j-1]
            else:   # already in the pattern index top, iterate haystack only now
                i += 1
    return -1



# haystack1 = "ABABDABACDABABCABAB"
# needle1 = "ABCDABCABCABABCFABCD"
# needle1 = 'aabaabaaa'

# print(create_pattern_string2(needle1))


# haystack1 = 'h3lloo'
# needle1 = 'el'
# haystack1="mississippi"
# needle1 = "oo"

haystack1 = "ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaabbbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb"
needle1 = "abbabbbabaa"
# print(strStr2(haystack1, needle1))

# needle1 = 'abcaby'
# haystack1 = 'abxabcabcaby'
print(strStr_kmp3(haystack1, needle1))
# print(strStr_kmp(haystack1, needle1))