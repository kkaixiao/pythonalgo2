"""
n a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}

        for i in time:
            d[i % 60] = d.get(i % 60, 0) + 1

        res = 0

        for k, v in d.items():

            if k == 0 or k == 30:
                res += v * (v - 1) // 2

            elif (60 - k) in d and (60 - k) > k:
                res += v * d[(60 - k)]

        return res