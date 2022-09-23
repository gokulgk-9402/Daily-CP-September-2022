#User function Template for python3

class Solution:
    def minLength(self, s, n): 
        #code here 
        stack = []
        mem = set(["12", "21", "34", "43", "56", "65", "78", "87", "09", "90"])
        
        for i in range(n):
            if stack == []:
                stack.append(s[i])
            else:
                temp = ""
                temp += stack[-1] + s[i]
                
                if temp in mem:
                    stack.pop()
                else:
                    stack.append(s[i])
                    
        return len(stack)