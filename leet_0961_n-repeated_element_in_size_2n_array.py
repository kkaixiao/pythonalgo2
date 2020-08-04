"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is
repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""

class Solution:
    # normal approach
    def repeatedNTimes(self, A: List[int]) -> int:
        d, n = {}, len(A)//2

        for num in A:
            preVal = d.get(num, 0)
            if preVal == n-1:
                return num
            d[num] = preVal + 1

    # use colllections.Counter class
    def repeatedNTimes(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        for key in cnt :
            if cnt[key] >=2 :
                return key
