class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem = [False] * (n + 1)

        for i in range(1, n+1):
            k = 1
            while k**2 <= i:
                if mem[i-k**2] == False:
                    mem[i] = True
                    break
                k += 1

        return mem[n]