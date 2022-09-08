#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None
'''

def summ(root, k):
    # code here
    inorder = []
    
    def inorder_traversal(node):
        if not node:
            return
        
        inorder_traversal(node.left)
        inorder.append(node.key)
        inorder_traversal(node.right)
    
    inorder_traversal(root)
    ans = 0
    for i in range(k):
        ans += inorder[i]
        
    return ans