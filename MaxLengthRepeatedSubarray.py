from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        mem = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    # print(i, j, m, n)
                    mem[i][j] = mem[i+1][j+1] + 1
        
        return max([max(row) for row in mem])

print(Solution().findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))