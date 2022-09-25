#User function Template for python3

class Solution:
    def solveQueries(self, n, Queries):
		# Code here

        matrix = [[0 for _ in range(n+2)] for _ in range(n+2)]
        rows = [[0 for _ in range(n+2)] for _ in range(n+2)]
        cols = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for query in Queries:
            a, b, c, d = query
            rows[a][b] += 1
            rows[c+1][b] -= 1
            cols[a][d+1] -=1
            cols[c+1][d+1] += 1
        for i in range(n):
            for j in range(1, n):
                rows[j][i] += rows[j-1][i]
                cols[j][i] += cols[j-1][i]

        for i in range(n):
            matrix[i][0] = rows[i][0] + cols[i][0]
        for i in range(1, n):
            for j in range(n):
                matrix[j][i] += matrix[j][i-1] + rows[j][i] + cols[j][i]

        ans = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[i][j] = matrix[i][j]

        return ans


print(Solution().solveQueries(n = 6,
Queries = [
[4,0,5,3],
[0,0,3,4]]))