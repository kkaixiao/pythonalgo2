"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original
BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
Note: This question is the same as 1038:
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return root

    def calcSum(self, node, currentSum):
        if not node:
            return currentSum

        node.val += self.calcSum(node.right, currentSum)

        return self.calcSum(node.left, node.val)


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.Sum = 0
        return self.calcInorder(root)

    def calcInorder(self, root):
        if root == None:
            return
        else:
            self.calcInorder(root.right)
            self.Sum += root.val
            root.val = self.Sum
            self.calcInorder(root.left)
            return root