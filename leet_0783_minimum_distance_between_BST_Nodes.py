"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between
the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between
node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = []
        diff = root.val + 1

        def getAllData(node, res):
            res.append(node.val)

            if not node.left and not node.right:
                return

            if node.left:
                getAllData(node.left, res)
            if node.right:
                getAllData(node.right, res)

        getAllData(root, res)
        res.sort()
        for i in range(len(res) - 1):
            diff = min(diff, abs(res[i] - res[i + 1]))

        return diff