"""
Given a binary tree, find the length of the longest path where each node in the path has the
same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.



Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2



Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2



Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more
than 1000.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        # keep track of longest univalue path
        longestPath = 0

        def calc(node):
            if not node:
                return 0

            else:

                pathLeft = calc(node.left)
                pathRight = calc(node.right)

                # if left node has the same value, extend path
                leftVal = pathLeft + 1 if node.left and node.left.val == node.val else 0

                # if right node has the same value, extend path
                rightVal = pathRight + 1 if node.right and node.right.val == node.val else 0

                nonlocal longestPath
                # use node as bridge to make univalue path as long as possible
                longestPath = max(longestPath, leftVal + rightVal)

                return max(leftVal, rightVal)

            # ------------------------------------------------

        calc(root)

        return longestPath