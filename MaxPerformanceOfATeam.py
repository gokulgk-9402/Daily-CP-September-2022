class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        current = 0
        heap = []
        ans = -1 * float('inf')
        
        for i, j in sorted(zip(efficiency, speed), reverse=True):
            while len(heap) > k - 1:
                current -= heappop(heap)
            
            heappush(heap, j)
            current += j
            ans = max(ans, current * i)
            
        return ans % (10**9 + 7)