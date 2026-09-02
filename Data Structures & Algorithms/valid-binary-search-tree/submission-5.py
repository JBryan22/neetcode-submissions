# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder = []

        def inorderTraversal(root: Optional[TreeNode]):
            if root == None:
                return
            
            inorderTraversal(root.left)
            inorder.append(root.val)
            inorderTraversal(root.right)
        
        for i in range(len(inorder), 1, 1):
            if inorder[i - 1] > inorder[i]:
                return False
        return True