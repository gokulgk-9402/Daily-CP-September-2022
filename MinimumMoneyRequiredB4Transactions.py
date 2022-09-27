from typing import List

class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
        profits = [x for x in transactions if x[1] >= x[0]]
        losses = [x for x in transactions if x[0] > x[1]]
        
        profits.sort(key= lambda x: -1 * x[0])
        losses.sort(key= lambda x: x[1])
        
        ans = 0
        curr = ans
            
        for loss in losses:
            if curr < loss[0]:
                ans += (loss[0] - curr)
                curr += (loss[0] - curr)
            
            curr -= loss[0]
            curr += loss[1]
        
        for profit in profits:
            if curr < profit[0]:
                ans += (profit[0] - curr)
                curr += (profit[0] - curr)
            
            curr -= profit[0]
            curr += profit[1]
            
        return ans
        