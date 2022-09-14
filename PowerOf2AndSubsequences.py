#User function Template for python3

class Solution:
    def numberOfSubsequences (ob,N,A):
        # code here 
        def ispower(num):
            while num != 1:
                if num%2:
                    return False
                num /= 2
                
            return True
            
        count = 0
        for n in A:
            if ispower(n):
                count += 1
        
        modulo = 10**9 + 7
        return (2**count - 1) % modulo