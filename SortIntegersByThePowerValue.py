class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        mem = {}

        temp = 1

        for i in range(lo, hi + 1):
            num = i
            power = 0

            while num > 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3 * num + 1
                power += 1
            
            mem[i] = power
        
        for key, val in sorted(mem.items(), key = lambda x: (x[1], x[0])):
            if temp == k:
                return key
            temp += 1


print(Solution().getKth(12, 15, 2))