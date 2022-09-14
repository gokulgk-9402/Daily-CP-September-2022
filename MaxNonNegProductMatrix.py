from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        maximums = [["#" for _ in range(n)] for _ in range(m)]
        minimums = [["#" for _ in range(n)] for _ in range(m)]
        
        maximums[m-1][n-1] = grid[-1][-1]
        minimums[m-1][n-1] = grid[-1][-1]

        for i in range(n-1, 0, -1):
            maximums[m-1][i-1] = grid[m-1][i-1] * maximums[m-1][i]
            minimums[m-1][i-1] = grid[m-1][i-1] * minimums[m-1][i]
            
        for i in range(m-1, 0, -1):
            maximums[i-1][n-1] = grid[i-1][n-1] * maximums[i][n-1]
            minimums[i-1][n-1] = grid[i-1][n-1] * minimums[i][n-1]

        # print(maximums)
        # print(minimums)

        def recursion(x, y):
            # print(x, y)

            if maximums[x][y] != '#' and minimums[x][y] != '#':
                return maximums[x][y], minimums[x][y]

            max1, min1 = recursion(x + 1, y)
            # print(x+1, y, max1, min1)
            
            max2, min2 = recursion(x, y + 1)
            # print(x, y+1, max2, min2)

            # print(max1, max2, min1, min2)

            maximum = max(max1, max2, min1, min2)
            minimum = min(max1, max2, min1, min2)

            if grid[x][y] < 0:
                maximums[x][y] = grid[x][y] * minimum
                minimums[x][y] = grid[x][y] * maximum
                return maximums[x][y], minimums[x][y]
            else:
                maximums[x][y] = grid[x][y] * maximum
                minimums[x][y] = grid[x][y] * minimum
                return maximums[x][y], minimums[x][y]

        val = max(recursion(0, 0))
        if val < 0:
            return -1

        return val % (10**9 + 7)

print(Solution().maxProductPath(grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))