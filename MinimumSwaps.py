from typing import List
class Solution:
    def minimumSwaps(self,c : List[int], v : List[int],n : int,k : int,b : int, t : int) -> int:
        # code here
        slow = 0
        ans = 0
        number = 0
        
        for i in range(n-1, -1, -1):
            pos = c[i] + v[i] * t
            if pos < b:
                slow += 1
            else:
                ans += slow
                number += 1
                if number == k:
                    return ans
                    
        return -1
    