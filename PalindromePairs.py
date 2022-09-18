class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        hashmap = {}
        
        for index, word in enumerate(words):
            hashmap[word] = index
            
        ans = set()
        
        for index, word in enumerate(words):
            if word == "":
                continue
                
            for j in range(len(word)):
                curr = word[:j]
                req = word[j:][::-1]
                if curr == curr[::-1] and req != word and req in hashmap:
                    ans.add((hashmap[req], index))
                    
            for j in range(len(word), -1, -1):
                curr = word[j:]
                req = word[:j][::-1]
                if curr == curr[::-1] and req != word and req in hashmap:
                    ans.add((index, hashmap[req]))
                    
            if word == word[::-1] and "" in hashmap:
                ans.add((index, hashmap[""]))
                ans.add((hashmap[""], index))
                
        return list(ans)