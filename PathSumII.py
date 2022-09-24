from typing import Optional, List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        
        def dfs(node, curr, currlist):
            if node.right == None and node.left == None:
                if curr + node.val == targetSum:
                    ans.append(currlist + [node.val])
                return
            
            if node.right:
                dfs(node.right, curr + node.val, currlist + [node.val])
            if node.left:
                dfs(node.left, curr + node.val, currlist + [node.val])
                    
        if root:
            dfs(root, 0, [])
            
        return ans
                