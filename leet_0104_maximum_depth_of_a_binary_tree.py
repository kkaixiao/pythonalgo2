"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0;
        if root.val is None:
            return 0

        else:

            # Compute the depth of each subtree
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)
            # print(lDepth, rDepth)

            # Use the larger one
            return max(lDepth, rDepth) + 1

    # if only one node in the tree, return 1