class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        i, j, k = 1, 1, 1
        mem = [1]
        two, three, five = 1, 1, 1
        
        for _ in range(n-1):
            ele = min(i*2, j*3, k*5)
            mem.append(ele)
            if ele == i*2:
                i = mem[two]
                two += 1
            if ele == j*3:
                j = mem[three]
                three += 1
            if ele == k*5:
                k = mem[five]
                five += 1
                
        return ele