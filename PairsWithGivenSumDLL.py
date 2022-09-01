from typing import Optional
from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        
        tail = head
        while tail.next:
            tail = tail.next
            
        ans = []
        while tail != head:
            curr = tail.data + head.data
            if curr == target:
                ans.append([head.data, tail.data])
                head = head.next
                
            elif curr < target:
                head = head.next
                
            else:
                tail = tail.prev
                
        return ans