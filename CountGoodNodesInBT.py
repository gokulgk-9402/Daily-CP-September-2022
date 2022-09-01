# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        goodnodes = 1
        
        def dfs(root, max_val):
            nonlocal goodnodes
            
            if root.val >= max_val:
                goodnodes += 1
                
            if root.left:
                dfs(root.left, max(root.val, max_val))
            
            if root.right:
                dfs(root.right, max(root.val, max_val))
                
        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)
            
        return goodnodes