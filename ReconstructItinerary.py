from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        n = len(tickets)
        ans = ["JFK"]

        for ele in tickets:
            graph[ele[0]].append(ele[1])
            
        def helper(source):
            nonlocal n
            if len(ans) == n + 1:
                return True

            if source not in graph:
                return False

            for index, destination in enumerate(graph[source]):
                if destination == "*":
                    continue

                graph[source][index] = "*"
                ans.append(destination)
                if helper(destination):
                    return True
                
                graph[source][index] = destination
                ans.pop()

            return False

        helper('JFK')
        return ans
            
print(Solution().findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))