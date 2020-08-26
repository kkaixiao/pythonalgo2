"""
Given words first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.



Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lText = text.split(' ')
        if len(lText) <= 2:
            return []
        res = []
        for i in range(len(lText)-2):
            if lText[i] == first and lText[i+1] == second:
                res.append(lText[i+2])
        return res