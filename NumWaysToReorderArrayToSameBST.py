from typing import List
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def recursion(lst):
            if len(lst) <= 1:
                return 1
             
            left = [num for num in lst if num < lst[0]]
            right = [num for num in lst if num > lst[0]]
            
            lw = recursion(left)
            rw = recursion(right)
            
            print(lw, rw)
            
            return (math.comb(len(left) + len(right), len(left)) * lw * rw) % MOD
        
        return (recursion(nums) - 1)