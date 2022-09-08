from collections import defaultdict, deque
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m, n = len(board), len(board[0])
        dic = defaultdict(set)

        for i in range(m):
            for j in range(n):
                dic[board[i][j]].add((i, j))

        results = deque()

        word, lngth, word_isReversed = '', 0, False
        def dfs(cord, indx):
            if indx == lngth: 
                if word_isReversed:
                    results.append(word[::-1])
                else:
                    results.append(word)
                return True

            ch = word[indx]
            i, j = cord
            for cand in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if cand in dic[ch]:
                    dic[ch].remove(cand)
                    flag = dfs(cand, indx + 1)
                    dic[ch].add(cand)
                    if flag: return True

            return False


        ref = set()
        for i in range(m):
            for j in range(n - 1):
                ref.add(board[i][j] + board[i][j + 1])
        for j in range(n):
            for i in range(m - 1):
                ref.add(board[i][j] + board[i + 1][j])

        #len_dic = len(dic)
        def check(word):
            for i in range(len(word) - 1):
                if word[i] + word[i + 1] not in ref:
                    if word[i + 1] + word[i] not in ref:
                        return False
            # wordCount = Counter(word)
            # if len(wordCount) > len_dic:
            #     return False
            # for ch, count in wordCount.items():
            #     if len(dic[ch]) < count:
            #         return False
            return True


        for w in words:
            if check(w):
                if w[:4] == w[0]*4 or len(dic[w[-1]]) < len(dic[w[0]]):
                    word = w[::-1]
                    word_isReversed = True
                else:
                    word = w
                    if word_isReversed: word_isReversed = False

                lngth = len(word)
                for cord in list(dic[word[0]]):
                    dic[word[0]].remove(cord)
                    flag = dfs(cord, 1)
                    dic[word[0]].add(cord)
                    if flag: break

        return results