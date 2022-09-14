from typing import Counter, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]

        while stack != []:
            node, path = stack.pop()
            # print(path)

            path = path ^ (1<< node.val)
            if node.left is None and node.right is None:
                if path & (path - 1) == 0:
                    ans += 1
            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        
        return ans

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

print(Solution().pseudoPalindromicPaths(root))
