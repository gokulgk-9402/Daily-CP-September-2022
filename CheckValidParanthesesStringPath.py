from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:

        m = len(grid)
        n = len(grid[0])

        mem = [[[False for i in range(m + n + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

        mem[m][n-1][0] = True
        mem[m-1][n][0] = True

        for r in range(m - 1, -1, -1):
            for c in range(n-1, -1, -1):
                for i in range(m + n):
                    nxt = -1 if grid[r][c] == ')' else 1
                    mem[r][c][i] = mem[r+1][c][i+nxt] or mem[r][c+1][i+nxt]

        return mem[0][0][0]

