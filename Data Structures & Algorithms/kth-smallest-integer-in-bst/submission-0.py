# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        currNode = root
        curI = 0

        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            
            currNode = stack.pop()
            curI += 1
            if curI == k:
                return currNode.val
            currNode = currNode.right
        
        return -1