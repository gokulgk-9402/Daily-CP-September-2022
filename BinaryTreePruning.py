from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recursion(node):
            if not node:
                return False
            
            v1 = recursion(node.right)
            
            v2 = recursion(node.left)
                
            if not v1:
                node.right = None
            if not v2:
                node.left = None
                
            return v1 or v2 or node.val
        
        if recursion(root):
            return root
        else:
            return None

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(Solution().pruneTree(root))