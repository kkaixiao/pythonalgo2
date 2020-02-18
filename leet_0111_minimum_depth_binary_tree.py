# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        # depth = float(1000000000000)
        depth = float('inf')
        stack = [(root, 1)]

        while stack:
            node, level = stack.pop()
            if node:

                if not node.left and not node.right:
                    depth = min(depth, level)

                stack.append((node.left, level+1))
                stack.append((node.right, level+1))

        return depth