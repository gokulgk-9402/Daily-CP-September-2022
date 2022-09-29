class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        neighbors = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        current = [1 for _ in range(10)]

        for _ in range(n - 1):
            next = [0 for _ in range(10)]
            for src in range(10):
                for dest in neighbors[src]:
                    next[dest] = (next[dest] + current[src]) % MOD
            current = next

        return sum(current) % MOD