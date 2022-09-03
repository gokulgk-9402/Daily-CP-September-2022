class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        def recursion(digits, diff, prev):
            if digits == 0:
                return [""]
            temp = []
            for i in range(10):
                if (prev - i == diff) or (i - prev == diff):
                    r = recursion(digits-1, diff, i)
                    for e in r:
                        temp.append(str(i) + e)
                        
            return temp
                    
        
        for i in range(1, 10):
            nxt = recursion(n-1, k, i)
            for res in nxt:
                a = str(i) + res
                ans.append(int(a))
                
        return ans
        