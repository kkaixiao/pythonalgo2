"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people
is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a
trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise,
return -1.


Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:
1. 1 <= N <= 1000
2. trust.length <= 10000
3. trust[i] are all different
4. trust[i][0] != trust[i][1]
5. 1 <= trust[i][0], trust[i][1] <= N
"""


class Solution:

    def findJudge1(self, n, trust):
        dict_respect = {}
        for i in range(n):
            dict_respect[i+1] = [0, 0]

        for item in trust:
            dict_respect[item[0]][0] += 1
            dict_respect[item[1]][1] += 1

        for i in range(n):
            if dict_respect[i+1][1] - dict_respect[i+1][0] == n-1:
                return i+1
        return -1

    def findJudge2(self, n, trust):
        dict_respect = {}
        dict_be_respected = {}
        for i in range(n):
            dict_respect[i+1] = 0
            dict_be_respected[i+1] = 0

        for item in trust:
            dict_respect[item[0]] += 1
            dict_be_respected[item[1]] += 1

        for i in range(n):
            if dict_respect[i+1] == 0 and dict_be_respected[i+1] == n-1:
                return i+1
        return -1


    def findJudge3(self, n, trust):
        arr_trust = [0] * n
        for i in range(len(trust)):
            trust_case = trust[i]
            arr_trust[trust_case[0] - 1] = -1
            if arr_trust[trust_case[1] - 1] >= 0:
                arr_trust[trust_case[1] - 1] += 1

        judge_idx = -1
        for i in range(n):
            if arr_trust[i] == n - 1:
                judge_idx = i
                break

        if judge_idx < 0:
            return -1
        else:
            return judge_idx + 1

    def findJudge4(self, n, trust):
        if n == 1:
            return 1
        res = -1
        arr_trust = [0] * (n+1)

        for case in trust:
            arr_trust[case[0]] += 1
            arr_trust[case[1]] -= 2
            if arr_trust[case[1]] == -2*(n-1):
                res = case[1]
        print(arr_trust)
        return res



# n1 = 4
# trust1 = [[1,3],[1,4],[2,3],[2,4],[4,3]]

# n1 = 2
# trust1 = [[1,2]]
#
# n1 = 3
# trust1 = [[1,3],[2,3]]
#
n1 = 3
trust1 = [[1,3],[2,3],[3,1]]
#
# n1 = 3
# trust1 = [[1,2],[2,3]]




mysolution = Solution()
print(mysolution.findJudge4(n1, trust1))