class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        # if input is empty, return 0
        if not nums:
            return None

        mid_idx = int(len(nums) / 2)

        root = TreeNode(nums[mid_idx])

        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx + 1:])

        return root