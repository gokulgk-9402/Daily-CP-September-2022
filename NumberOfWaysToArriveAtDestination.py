from typing import List
from collections import defaultdict
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        source = 0
        destination = n - 1
        
        graph = defaultdict(list)
        
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
            
        distances = [[float('inf'), 0] for i in range(n)]
        distances[source] = [0, 1]
        
        not_visited = set(graph.keys())
        
        while not_visited:
            curr = None
            
            for node in not_visited:
                if curr is None:
                    curr = node
                    
                elif distances[node][0] < distances[curr][0]:
                    curr = node
                    
            for neighbor, w in graph[curr]:
                curr_distance = distances[curr][0] + w
                if curr_distance < distances[neighbor][0]:
                    distances[neighbor][0] = curr_distance
                    distances[neighbor][1] = distances[curr][1]
                
                elif curr_distance == distances[neighbor][0]:
                    distances[neighbor][1] += distances[curr][1]
                
            not_visited.remove(curr)
            
        return distances[destination][1] % (10**9 + 7)