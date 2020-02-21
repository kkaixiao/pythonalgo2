class Solution:
    def getRow(self, r):

        res = [1] * (r+1)

        for i in range(1, r+1):
            res[i] = res[i-1] * (r+i-1)//i

        return res