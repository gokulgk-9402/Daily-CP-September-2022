import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        mem = collections.defaultdict(list)

        if beginWord not in wordList:                
            wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                mem[pattern].append(word)

        visited = set(beginWord)
        q = collections.deque([beginWord])
        ans = 1

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return ans

                for j in range(len(word)):
                    pattern = curr[:j] + "*" + curr[j+1:]
                    for nextWord in mem[pattern]:
                        if nextWord not in visited:
                            visited.add(nextWord)
                            q.append(nextWord)

            ans +=1
        
        return 0