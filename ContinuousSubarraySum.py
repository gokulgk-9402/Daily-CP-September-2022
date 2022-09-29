class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) == 1:
            return False
        
        hashmap = {0: 0}
        length = len(nums)
        curr = 0
        for i in range(length):
            curr += nums[i]
            curr %= k
            
            if curr % k not in hashmap:
                hashmap[curr] = i + 1
            elif hashmap[curr] < i:
                return True
            
        return False
            
        