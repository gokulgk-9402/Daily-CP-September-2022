class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        mem = '1'
        i = 2
        while i <= n:
            mem += str(bin(i))[2:]
            i += 1
        
        return int(mem, 2) % MOD