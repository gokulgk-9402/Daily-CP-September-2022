from typing import List
from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        mem = defaultdict(list)
        maximum = 0
        for n in arr:
            string = str(bin(n))[2:]
            count = 0
            for char in string:
                if char == '1':
                    count += 1
            if count > maximum:
                maximum = count
            mem[count].append(n)
            
        ans = []
        for key in range(maximum + 1):
            ans = ans + mem[key]
            
        return ans