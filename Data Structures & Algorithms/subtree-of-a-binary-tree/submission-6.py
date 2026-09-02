# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            stack1 = [root1]
            stack2 = [root2]

            while stack1 or stack2:
                if not stack1 or not stack2:
                    return False
                node1 = stack1.pop()
                node2 = stack2.pop()

                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack1.append(node1.right)
                stack2.append(node2.right)
            return True
                
        
        stack = [root]

        while stack:
            node = stack.pop()

            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    
