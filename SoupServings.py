class Solution:
    def soupServings(self, n: int) -> float:

        mem = [[-1] * 192 for _ in range(192)]

        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if mem[a][b] != -1:
                return mem[a][b]

            mem[a][b] = 0.25 * (dfs(a-4,b) + dfs(a-3,b-1) + dfs(a-2,b-2) + dfs(a-1,b-3))

            return mem[a][b]

        if n >= 4800:
            return 1
        
        return dfs((n+24)//25, (n+24)//25)