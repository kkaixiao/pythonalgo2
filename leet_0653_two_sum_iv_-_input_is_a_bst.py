"""
Given a Binary Search Tree and a target number, return true if there exist two elements in
the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.dicNums = dict()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root:
            if root.val in self.dicNums:
                return True
            self.dicNums[k - root.val] = root.val

            return self.findTarget(root.left, k) or self.findTarget(root.right, k)