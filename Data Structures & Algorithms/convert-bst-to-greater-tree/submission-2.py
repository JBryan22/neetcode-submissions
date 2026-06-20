# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total_sum = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
        
            curr = stack.pop()

            total_sum += curr.val
            curr.val = total_sum

            curr = curr.left
            
        return root
        