"""
Given a binary search tree with non-negative values, find the minimum absolute difference
between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note:

There are at least two nodes in this BST.
This question is the same as
783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return None

        res = []

        def saveToList(node):
            if not node:
                return

            saveToList(node.left)
            res.append(node.val)
            saveToList(node.right)

        saveToList(root)
        return min(abs(res[i + 1] - res[i]) for i in range(len(res) - 1))

