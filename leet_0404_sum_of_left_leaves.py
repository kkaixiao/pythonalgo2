"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        return total + self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)


    # BFS
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0

        total = 0
        queue = [root]

        while queue:
            curr = queue.pop(0)
            # check if there's a left leaf
            if curr.left and not curr.left.left and not curr.left.right:
                total += curr.left.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return total


    # the following is for DFS
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = []
        self.dfs(root)
        return sum(self.res)

    def dfs(self, root):

        if not root:
            return root

        if root.left and not root.left.left and not root.left.right:
            self.res.append(root.left.val)

        root.left = self.dfs(root.left)
        root.right = self.dfs(root.right)