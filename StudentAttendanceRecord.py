class Solution:
    def checkRecord(self, s: str) -> bool:
        
        numA = 0
        numL = 0
        maxL = 0
        
        i = 0
        while i < len(s):
            if s[i] == 'A':
                numA += 1
            elif s[i] == 'L':
                numL = 0
                while i < len(s) and s[i] == 'L':
                    numL += 1
                    i += 1

                if numL > maxL:
                    maxL = numL
                i -= 1
                
            i += 1
            
        if numA < 2 and maxL < 3:
            return True
        
        return False
                    