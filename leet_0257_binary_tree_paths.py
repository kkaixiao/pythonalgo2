"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.getPath(root, '')

    def getPath(self, root, cur_path):
        if not root:
            return []

        if not root.left and not root.right:
            return [cur_path + str(root.val)]

        cur_path += str(root.val) + '->'

        return self.getPath(root.left, cur_path) + self.getPath(root.right, cur_path)