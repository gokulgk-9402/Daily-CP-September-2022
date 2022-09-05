class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)
        len_w2 = len(word2)

        mem = [[0 for _ in range(len_w1 + 1)] for _ in range(len_w2 + 1)]

        for i in range(len_w1):
            mem[len_w2][i] = len_w2 - 1
        for i in range(len_w2):
            mem[i][len_w1] = len_w1 - 1

        for i in range(len_w2 - 1, -1, -1):
            for j in range(len_w1 - 1, -1, -1):
                if word1[j] == word2[i]:
                    mem[i][j] = mem[i + 1][j + 1]
                else:
                    mem[i][j] = min(mem[i + 1][j], mem[i + 1][j + 1], mem[i][j + 1]) + 1

        return mem[0][0]

print(Solution().minDistance(word1 = "intention", word2 = "execution"))