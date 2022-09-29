from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        number = len(s)
        length = 0
        index = 0
        for i in range(number):
            if len(s[i]) >= length:
                index = i
                length = len(s[i])
                
        ans = [""] * length

        for i in range(len(s)):
            temp = len(s[i])
            for j in range(temp):
                ans[j] += s[i][j]
            for j in range(temp, length):
                ans[j] += ' '

        for i in range(length):
            while ans[i][-1] == ' ':
                ans[i] = ans[i][:-1]

        return ans

print(Solution().printVertically(s = "CONTEST IS COMING"))