# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def pathSum(root: Optional[TreeNode], targetSum: int, currSum: int):
            if not root:
                return False

            currSum += root.val
            if root.left == None and root.right == None and currSum == targetSum:
                return True
            
            if pathSum(root.left, targetSum, currSum):
                return True
            if pathSum(root.right, targetSum, currSum):
                return True
            
            currSum -= root.val
            return False
        
        return pathSum(root, targetSum, 0)
