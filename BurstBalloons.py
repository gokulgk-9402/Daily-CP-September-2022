class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        
        mem = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        
        for i in range(n, 0, -1):
            for j in range(1, n + 1):
                if i <= j:
                    maximum = float('-inf')
                    for index in range(i, j + 1):
                        curr = nums[i-1]*nums[index]*nums[j+1] + mem[i][index-1] + mem[index+1][j]
                        maximum = max(maximum, curr)
                    mem[i][j] = maximum
                
        return mem[1][n]