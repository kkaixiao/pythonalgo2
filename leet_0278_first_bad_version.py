"""
You are a product manager and currently leading a team to develop a new product. Unfortunately,
the latest version of your product fails the quality check. Since each version is developed based
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes
all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement
a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n

        start = 1
        end = n

        while start < end:

            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1

        return start

    def firstBadVersion3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n

        res = start = 1



        while start < n:
            if isBadVersion(res):
                start = res
            else:
                start += 1

        return start

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return n
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                if isBadVersion(mid + 1):
                    return mid + 1
                start = mid
            elif isBadVersion(mid):
                if mid == 1:
                    return 1
                elif not isBadVersion(mid - 1):
                    return mid
                end = mid

    def firstBadVersion_rec(self, n):
        return self.recursive(1, n)

    def recursive(self, start, end):
        if start == end:
            return start

        if isBadVersion(mid):
            return self.recursive(start+1, end)
        else:
            return self.recursive(start, end-1)


    def recursive_slow(self, start, end):
        if start == end:
            return start

        if not isBadVersion(start):
            return self.recursive(start + 1, end)
        else:

            return start