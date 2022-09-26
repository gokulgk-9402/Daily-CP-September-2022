from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        
    def find(self, node):
        if self.parents[node] == -1:
            return node
        
        return self.find(self.parents[node])
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        
        if parent1 != parent2:
            self.parents[parent1] = parent2
            

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for equation in equations:
            if equation[1] == "!":
                continue
            uf.union(equation[0], equation[-1])
               
        return not any(uf.find(equation[0]) == uf.find(equation[-1]) for equation in equations if equation[1] == '!')