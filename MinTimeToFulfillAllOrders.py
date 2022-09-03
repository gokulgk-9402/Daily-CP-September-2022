from typing import List
class Solution:
    def findMinTime(self, n : int, l : int, arr : List[int]) -> int:
        
        def number(days):
            count = 0
            for i in range(l):
                c = 0
                time = days
                time_per_donut = arr[i]
                
                while time > 0:
                    time -= time_per_donut
                    if time >= 0:
                        c += 1
                        time_per_donut += arr[i]
                        
                count += c
                
            return count
        
        # code here
        left = 1
        right = 10000007
        
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if number(mid) < n:
                left = mid + 1
                
            else:
                ans = mid
                right = mid - 1
                
        return ans