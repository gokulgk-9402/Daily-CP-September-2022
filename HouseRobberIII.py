from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node is None:
                return 0, 0
            
            left, pre_left = dfs(node.left)
            right, pre_right = dfs(node.right)
            
            return max(left + right, node.val + pre_left + pre_right), left + right
        
        return dfs(root)[0]