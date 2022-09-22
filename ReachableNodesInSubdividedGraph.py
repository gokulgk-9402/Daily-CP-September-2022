import collections
import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        priorityq = [(0, 0)]
        distances = {0:0}
        used = {}

        ans = 0

        while priorityq:
            dist, node = heapq.heappop(priorityq)
            if dist > distances[node]:
                continue
            ans += 1

            for neighbor, weight in graph[node].items():
                v = min(weight, maxMoves - dist)
                used[node, neighbor] = v

                d2 = dist + weight + 1
                if d2 < distances.get(neighbor, maxMoves + 1):
                    heapq.heappush(priorityq, (d2, neighbor))
                    distances[neighbor] = d2

        for u, v, w in edges:
            ans += min(w, used.get((u,v), 0) + used.get((v, u), 0))

        return ans


print(Solution().reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))