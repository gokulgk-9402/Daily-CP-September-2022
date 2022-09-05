"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        queue = []
        levels = []
        
        if not root:
            return []
        
        queue.append((root, 0))
        
        while queue != []:
            ele, lvl = queue.pop(0)
            if lvl < len(levels):
                levels[lvl].append(ele.val)
            else:
                while len(levels) < lvl + 1:
                    levels.append([])
                levels[lvl].append(ele.val)
            
            if ele.children:
                for child in ele.children:
                    queue.append((child, lvl + 1))
                    
        return levels
        