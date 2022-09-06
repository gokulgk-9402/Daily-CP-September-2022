#User function Template for python3

class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        
        ans = 0
        for i in range(N):
            diff = A[i] - B[i]
            if diff < 0:
                diff *= -1
            ans += diff
            
        return ans