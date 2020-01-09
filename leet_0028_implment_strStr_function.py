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

    i = 0  # index for txt[]
    while i < m:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == n:
            print("Found pattern at index " + str(i - j))
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


haystack1 = "ABABDABACDABABCABAB"
needle1 = "ABABCABAB"
print(strStr_kmp(haystack1, needle1))



# # haystack1 = 'hello'
# # needle1 = 'll'
# haystack1="mississippi"
# needle1="pi"
#
# print(strStr2(haystack1, needle1))