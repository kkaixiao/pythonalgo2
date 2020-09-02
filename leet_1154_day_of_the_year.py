"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.



Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61


Constraints:9

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""

class Solution:
    def dayOfYear(self, date: str) -> int:
        calender = date.split('-')
        year, month, day = int(calender[0]), int(calender[1]), int(calender[2])
        monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        preMonthDay = sum(monthday[:month - 1])

        if year % 4 == 0 and month > 2 and year != 1900:
            preMonthDay += 1

        return preMonthDay + day