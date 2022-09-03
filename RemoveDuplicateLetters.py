class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occurences = {}
        stack = []
        current = {}
        
        n = len(s)
        
        for i in range(n):
            last_occurences[s[i]] = i
            current[s[i]] = False
        
        # print(last_occurences)
            
        for i in range(n):
            # print(stack)
            if not current[s[i]]:
                while (stack and stack[-1] > s[i] and last_occurences[stack[-1]] > i):
                    current[stack.pop()] = False
                    
                stack.append(s[i])
                current[s[i]] = True
                
        return "".join(stack)

print(Solution().removeDuplicateLetters("bcabc"))