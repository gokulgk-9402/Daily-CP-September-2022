class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
            
        if res == 0:
            return True
        
        return False