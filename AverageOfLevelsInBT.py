# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return [0]
        
        levels = []
        
        queue = [(root, 0)]
        
        while queue != []:
            node, curr = queue.pop(0)
            
            if curr == len(levels):
                levels.append([node.val])
            else:
                levels[curr].append(node.val)
                
            if node.left:
                queue.append((node.left, curr + 1))
                
            if node.right:
                queue.append((node.right, curr + 1))
                
        for i in range(len(levels)):
            levels[i] = sum(levels[i]) / len(levels[i])
            
        return levels