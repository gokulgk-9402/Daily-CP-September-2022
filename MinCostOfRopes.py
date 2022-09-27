#User function Template for python3
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        heapq.heapify(arr)
        ans = 0
        while len(arr) != 1:
            val = heapq.heappop(arr)
            val += heapq.heappop(arr)
            
            ans += val
            heapq.heappush(arr, val)
            
        return ans
            