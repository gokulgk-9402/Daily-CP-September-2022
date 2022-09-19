from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        mem = [(nums[i], i) for i in range(len(nums))]

        mem = sorted(mem)
        
        return [ t[0] for t in sorted(mem[-k:], key = lambda x: x[1])]

print(Solution().maxSubsequence(nums = [2,1,3,3], k = 2))