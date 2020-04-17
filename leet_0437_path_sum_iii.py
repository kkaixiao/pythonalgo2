
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to
1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


class Solution:

    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        d = {}
        d[0] = 1

        self.target = s
        self.count = 0

        self.dfs(root, 0, d)
        return self.count

    def dfs(self, node, pre, dic):

        if node is None:
            return

        curSum = pre + node.val

        if curSum-self.target in dic:
            self.count += dic[curSum-self.target]

        if curSum not in dic:
            dic[curSum] = 0
        dic[curSum] += 1

        self.dfs(node.left, curSum, dic)
        self.dfs(node.right, curSum, dic)

        dic[curSum] -= 1