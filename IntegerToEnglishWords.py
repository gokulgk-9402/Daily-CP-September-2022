class Solution:
    def numberToWords(self, num: int) -> str:
        tens = {2: 'Twenty', 3:'Thirty', 4:'Forty',5:'Fifty',6:'Sixty', 7:'Seventy', 8: 'Eighty', 9: 'Ninety'}
        ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        odd = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        
        col = {1: 'Thousand', 2: 'Million', 3: 'Billion'}
        if num == 0:
            return "Zero"
        
        def generate(n):
            hs = n // 100
            ts = (n%100) // 10
            os = (n%10)
            
            res = ""
            if hs:
                res += ones[hs] + ' Hundred '
            # print(ts, n)
            if ts > 1:
                res += tens[ts]
                if os:
                    res += ' ' + ones[os]            
                return res
            elif ts == 0:
                if os:
                    res += ones[os]
                return res
            else:
                key = n%100
                res += odd[key]
                return res
        
        temp = num
        arr = []
        while temp != 0:
            arr.append(temp%1000)
            temp = temp // 1000
        
        ans = ""
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != 0:
                ans += generate(arr[i])
                if i != 0:
                    ans += ' ' + col[i]
                ans += ' '
                
        return ' '.join(x for x in ans.split() if x != '')