import math

class Solution:
    def distinctSequences(self, n: int) -> int:
        dp = [[[-1 for _ in range(10 ** 4 + 5)] for _ in range(7)] for _ in range(7)]
        
        def helper(prev2: int, prev1: int, idx: int, sz: int) -> int:
            if idx == sz:
                return 1
            if dp[prev2][prev1][idx] != -1:
                return dp[prev2][prev1][idx] % (10 ** 9 + 7)
            ans = 0
            for cur in range(1, 7):
                if cur != prev2 and cur != prev1 and (prev1 == 0 or math.gcd(cur, prev1) == 1):
                    ans = ans + helper(prev1, cur, idx + 1, sz)
            dp[prev2][prev1][idx] = ans
            return ans % (10 ** 9 + 7)
        
        return helper(0, 0, 0, n)

print(Solution().distinctSequences(4))