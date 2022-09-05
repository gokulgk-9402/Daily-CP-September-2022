#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        min_ending = float('inf')
        minimum = float('inf')
        
        for i in range(N):
            if min_ending > 0:
                min_ending = A[i]
            else:
                min_ending += A[i]
        
            minimum = min(min_ending, minimum)
        
        return minimum