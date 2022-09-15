class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2:
            return []
        
        mem = Counter(changed)
        ans = []
        
        for x in sorted(changed):
            if mem[x] > mem[x*2]:
                return []
            
            if x == 0:
                if mem[x] % 2:
                    return []
                else:
                    ans += [0] * (mem[x]//2)
            else:
                ans += [x] * mem[x]
            
            mem[2*x] -= mem[x]
            mem[x] = 0
            
        return ans