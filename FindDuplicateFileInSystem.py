from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for path in paths:
            directory = path.split(' ')[0]
            files = path.split(' ')[1:]
            for file in files:
                filename = file.split('(')[0]
                content = file.split('(')[1]
                content = content[:-1]
                fullpath = directory + '/' + filename
                hashmap[content].append(fullpath)
                
        ans = []
        for key in hashmap:
            if len(hashmap[key]) > 1:
                ans.append(hashmap[key])
                
        return ans