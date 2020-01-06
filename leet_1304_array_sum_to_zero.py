"""
Given an integer n, return any array containing n unique integers such that they add
up to 0.



Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]


Constraints:

1 <= n <= 1000
"""

def sum_zero(n):
    if n > 1000 or n < 1:
        return []

    res = []
    for i in range(n//2):
        res.append(-i-1)
    for i in range(n//2, n-1):
        res.append(n-i-1)

    if n % 2 != 0:
        res.append(0)
    else:
        res.append(n//2)

    return res

print(sum_zero(7))