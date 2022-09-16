import itertools
from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:
            return -1
        
        accum = [0] + list(itertools.accumulate(stones))
        
        mem = [[0 for _ in range(n)] for _ in range(n)]
        
        for l in range(k, n + 1):
            for i in range(n-l + 1):
                j = i + l - 1
                if l > k:
                    mem[i][j] = min([mem[i][t] + mem[t+1][j] for t in range(i, j, k - 1)])
                if (l-k)%(k-1) == 0:
                    mem[i][j] += accum[j+1] - accum[i]
                    
        return mem[0][n-1]