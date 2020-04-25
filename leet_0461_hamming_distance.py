"""
The Hamming distance between two integers is the number of positions at which the
corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        binx, biny = bin(x)[2:], bin(y)[2:]
        maxlen = max(len(binx), len(biny))

        # the first zero padding method
        binx, biny = '%0*d' % (maxlen, int(binx)), '%0*d' % (maxlen, int(biny))

        # second zero padding method
        # binx, biny = binx.zfill(maxlen), biny.zfill(maxlen)

        # third (manual) padding method
        # if len(binx) > len(biny):
        #     for k in range(len(binx)-len(biny)):
        #         biny = '0' + biny
        # elif len(biny) > len(binx):
        #     for k in range(len(biny)-len(binx)):
        #         binx = '0' + binx

        count = 0
        for i in range(maxlen):
            if binx[i] != biny[i]:
                count += 1

        return count