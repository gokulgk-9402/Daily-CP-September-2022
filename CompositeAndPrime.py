#User function Template for python3

class Solution:
    def Count(self, L, R):
		# Code here
        prime = [1] * (R + 1)
        prime[0] = False
        prime[1] = False
        
        i = 2
        while i * i <= R:
            if prime[i]:
                for j in range(i*i, R+1, i):
                    prime[j] = False
            i += 1
            
        ans = 0
        for i in range(L, R + 1):
            if prime[i]:
                ans += 1
            
        ans = R - L + 1 - 2*ans
        
        if L == 1:
            return ans - 1
        
        return ans