#User function Template for python3

class Solution:
    def findOccurrence(self,mat,target):
        
        rows = len(mat)
        cols = len(mat[0])
        
        ans = 0
        
        def dfs(x, y, matrix, word, curr):
            nonlocal rows, cols
                
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return 0
            
            if word[curr] != matrix[x][y]:
                return 0
                
            found = 0
            curr += 1
            temp = matrix[x][y]
            matrix[x][y] = 0
            
            if curr == len(word):
                found = 1
            else:
                found += dfs(x+1,y, matrix, word, curr)
                found += dfs(x, y+1, matrix, word, curr)
                found += dfs(x-1, y, matrix, word, curr)
                found += dfs(x, y-1,matrix, word, curr)
                
            matrix[x][y] = temp
                
            return found
        
        for i in range(rows):
            for j in range(cols):
                ans += dfs(i,j, mat, target, 0)
                    
        return ans

print(Solution().findOccurrence(
mat = [['S','N','B','S','N'],
       ['B','A','K','E','A'],
       ['B','K','B','B','K'],
       ['S','E','B','S','E']],
target = 'SNAKES'))