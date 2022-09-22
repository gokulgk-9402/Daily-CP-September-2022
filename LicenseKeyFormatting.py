#User function Template for python3

class Solution:
    def ReFormatString(self,S, K):
        #code here
        S = "".join(S.split('-'))
        length = len(S)
        ans = ""
        i = length % K

        ans += S[:i]
        if i:
            ans += '-'
        
        while i < length:
            ans += S[i:i+K]
            ans += '-'
            i += K

        if ans != "" and ans[-1] == '-':
            ans = ans[:-1]
        
        return ans.upper()


print(Solution().ReFormatString(S = "-", K = 4))