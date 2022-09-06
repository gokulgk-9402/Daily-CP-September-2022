# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def recursion(node, minimum, maximum):
            if not node:
                return maximum - minimum
            
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            
            return max(recursion(node.right, minimum, maximum), recursion(node.left, minimum, maximum))
        
        return recursion(root, root.val, root.val)