#User function Template for python3

class Solution:
    def minSubset(self, A,N):
        A.sort()
        total = sum(A) / 2

        mem = 0
        for i in range(N):
            if mem + A[i] < total:
                mem += A[i]
            else:
                return N - i

print(Solution().minSubset([20, 12, 18, 4], 4))