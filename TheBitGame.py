#User function Template for python3

class Solution:
    def swapBitGame (self,N):
        # code here 
        
        no_ones = 0
        
        while N != 0:
            no_ones += N % 2
            N = N // 2
            
        if no_ones % 2:
            return 1
        else:
            return 2