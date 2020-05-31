"""
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so
that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree,
so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trimNode(node):
            if not node:
                return
            if node.val < L:
                return trimNode(node.right)
            elif node.val > R:
                return trimNode(node.left)
            else:
                node.left, node.right = trimNode(node.left), trimNode(node.right)
                return node
        return trimNode(root)