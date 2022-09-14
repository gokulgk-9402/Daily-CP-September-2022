from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        mem = {}
        mem[(m-1, n-1)] = (grid[-1][-1], grid[-1][-1])
        for i in range(n-1, 0, -1):
            mem[(m-1, i-1)] = grid[m-1][i-1] * mem[(m-1, i)][0], grid[m-1][i-1] * mem[(m-1, i)][0]
        for i in range(m-1, 0, -1):
            mem[(i-1, n-1)] = grid[i-1][n-1] * mem[(i, n-1)][0], grid[i-1][n-1] * mem[(i, n-1)][0]

        # print(mem)

        def recursion(x, y):
            # print(x, y)

            if (x,y) in mem:
                return mem[(x,y)]

            max1, min1 = recursion(x + 1, y)
            # print(x+1, y, max1, min1)
            
            max2, min2 = recursion(x, y + 1)
            # print(x, y+1, max2, min2)

            maximum = max(max1, max2, min1, min2)
            minimum = min(max1, max2, min1, min2)

            if grid[x][y] < 0:
                mem[(x,y)] = grid[x][y] * minimum, grid[x][y] * maximum
                return mem[(x,y)]
            else:
                mem[(x,y)] = grid[x][y] * maximum, grid[x][y] * minimum
                return mem[(x,y)]

        val = max(recursion(0, 0))
        if val < 0:
            return -1

        return val % (10**9 + 7)

print(Solution().maxProductPath(grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))