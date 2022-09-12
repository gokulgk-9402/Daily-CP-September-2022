from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mem = defaultdict(list)
        
        for ele in tickets:
            mem[ele[0]].append(ele[1])
            
        # print(mem)
            
        ans = []
        
        n = len(mem)
        curr = 'JFK'
        ans.append(curr)
        while len(ans) <= n:
            # print(mem[curr])
            curr = min(mem[curr])
            ans.append(curr)
            
        return ans
print(Solution().findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))