# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        
        queue = [(root, 0, 0)]
        
        while queue:
            node, row, col = queue.pop(0)
            res[(row, col)].append(node.val)
            res[(row, col)].sort()
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
                
        ans = defaultdict(list)
        keys = sorted(list(res.keys()), key = lambda x: (x[0], x[1]))
        
        for k in keys:
            row, col = k
            res[col].extend(res[k])
            
        return list(ans.values())