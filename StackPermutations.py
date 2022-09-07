

from typing import List
class Solution:
    def isStackPermutation(self, N : int, A : List[int], B : List[int]) -> int:
        # code here
        i = 0
        j = 0
        stack = []
        
        while j < N:
            stack.append(A[j])
            while i < N and stack != [] and stack[-1] == B[i]:
                if i == N - 1:
                    return 1
                i += 1
                stack.pop(-1)
            j += 1
            
        return 0

