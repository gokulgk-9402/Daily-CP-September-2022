from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        
        m = 10**9 + 7
        
        length = len(nums)
        nums.sort()
        
        powers_of_2 = [1]
        for i in range(1, length):
            powers_of_2.append(powers_of_2[-1] * 2 % m)
            
        ans = 0
        for i in range(length):
            ans = (ans + (powers_of_2[i] - powers_of_2[length-i-1]) * nums[i]) % m
            
        return ans

print(Solution().sumSubseqWidths([2, 1, 3]))