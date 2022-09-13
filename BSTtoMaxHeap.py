
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def convertToMaxHeapUtil(self, root):
        #code here
        inorder = []
        
        def in_trav (root):
            if not root:
                return
            
            in_trav(root.left)
            inorder.append(root.data)
            in_trav(root.right)
        
        ptr = 0
            
        def to_heap(root):
            # print(arr)
            nonlocal ptr
            if root == None:
                return None
                
            root.left = to_heap(root.left)
            root.right = to_heap(root.right)
            root.data = inorder[ptr]
            ptr += 1
            
            return root
        
        in_trav(root)
        # print(inorder)
        root = to_heap(root)
        return root

root = Node(4)
root.right = Node(6)
root.left = Node(2)
root.right.right= Node(7)
root.right.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

r = Solution().convertToMaxHeapUtil(root)