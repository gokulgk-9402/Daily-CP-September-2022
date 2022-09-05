class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        length = len(s)
        flags = [0 for _ in range(length)]
        
        i = 0
        while i < length:
            if s[i] == '(':
                stack.append(i)
            else:
                if stack != []:
                    flags[i] = 1
                    flags[stack.pop(-1)] = True
            
            i += 1
            
        current = 0
        longest = 0
        
        for flag in flags:
            if flag:
                current += 1
            else:
                longest = max(current, longest)
                current = 0
                
        return max(longest, current)