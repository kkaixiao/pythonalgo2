"""

"""


class Solution:
    # with the use of dictionary
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        d = dict()
        for i in range(len(widths)):
            d[chr(i + 97)] = widths[i]

        line, count = 1, 0

        for c in S:
            if count + d[c] <= 100:
                count += d[c]
            else:
                line += 1
                count = d[c]

        return [line, count]

    # without the use of dictionary
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line, count = 1, 0
        units = 100

        for letter in S:
            index = ord(letter) - 97
            diff = units - widths[index]

            if (diff < 0):
                line += 1
                units = 100 - widths[index]
            else:
                units = diff

        count = 100 - units

        return [line, count]