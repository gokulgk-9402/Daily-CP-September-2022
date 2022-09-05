class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            v1 = min(a, b)
            v2 = max(a, b)

            if v1 == 0:
                return v2

            tmp = gcd(v2%v1, v1)
            return tmp
        
        sign = 1
        
        lst = []
        length = len(expression)
        
        i = 0
        
        while i < length:
            if expression[i] == '+':
                sign = 1
            elif expression[i] == '-':
                sign = -1
            else:
                curr = expression[i]
                if sign == -1:
                    curr = '-' + curr
                    sign = 1
                i += 1
                while i < length and expression[i] != '+' and expression[i] != '-':
                    curr += expression[i]
                    i += 1
                lst.append(curr)
                continue
            i += 1
            
        numers = []
        denoms = []
        
        prod_denom = 1
        numbers = 0
        
        for ele in lst:
            num, den = ele.split('/')
            numers.append(int(num))
            denoms.append(int(den))
            prod_denom *= int(den)
            numbers += 1
            
        for i in range(numbers):
            numers[i] = numers[i] * (prod_denom//denoms[i])
            
        res_num = sum(numers)
        res_denom = prod_denom
        
        sign = 1
        
        if res_num < 0:
            sign = -1
            res_num = res_num * -1
        
        g = gcd(res_num, res_denom)
        
        ans = ""
        if sign == -1:
            ans += '-'
        ans += str(res_num//g)
        ans += '/'
        ans += str(res_denom//g)
        
        return ans