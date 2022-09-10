from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0: 
            return 0
        
        mem = [[1000, 0] for _ in range(k + 1)]
        
        for price in prices:
            for i in range(1, k + 1):
                mem[i][0] = min(mem[i][0], price - mem[i - 1][1])
                mem[i][1] = max(mem[i][1], price - mem[i][0])
                
        return mem[k][1]