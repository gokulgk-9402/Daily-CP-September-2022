class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occurences = {}
        stack = []
        current = set()
        
        n = len(s)
        
        for i in range(n):
            last_occurences[s[i]] = i
        
        print(last_occurences)
            
        for i in range(n):
            print(stack)
            if s[i] not in current:
                while (stack and stack[-1] > s[i] and last_occurences[stack[-1]] > i):
                    current.remove(stack.pop())
                    
                stack.append(s[i])
                current.add(s[i])
                
        return "".join(stack)