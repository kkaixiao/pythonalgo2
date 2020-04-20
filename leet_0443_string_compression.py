"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0

        while j < len(chars):
            count, k = 1, j + 1

            while k < len(chars) and chars[j] == chars[k]:
                count, k = count + 1, k + 1

            chars[i] = chars[j]
            i += 1

            if count > 1:
                for char in str(count):
                    chars[i], i = char, i + 1

            j = k

        return i
