from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        if height == []:
            return 0
        
        ans = 0
        length = len(height)
        
        left = [0] * length
        right = [0] * length
        
        left[0] = height[0]
        for i in range(1, length):
            left[i] = max(height[i], left[i-1])
            
        right[-1] = height[-1]
        for i in range(length-2, -1, -1):
            right[i] = max(right[i+1], height[i])
            
        for i in range(length-1):
            ans += min(left[i], right[i]) - height[i]
            
        return ans