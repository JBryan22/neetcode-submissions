# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.totalVal = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.convertBST(root.right)
            self.totalVal += root.val
            root.val = self.totalVal
            self.convertBST(root.left)
        return root