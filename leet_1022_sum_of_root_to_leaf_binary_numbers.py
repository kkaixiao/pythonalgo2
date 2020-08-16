"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number
 starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then
 this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        self.pathes, self.binarySum = [], 0

        def goThrough(node, pathStr):

            if node.left:
                goThrough(node.left, pathStr + str(node.val))

            if node.right:
                goThrough(node.right, pathStr + str(node.val))

            if not node.left and not node.right:
                pathStr += str(node.val)
                self.pathes.append(pathStr)
                self.binarySum += int(pathStr, 2)

        goThrough(root, "")

        return self.binarySum