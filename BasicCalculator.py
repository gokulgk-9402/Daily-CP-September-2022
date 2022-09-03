class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        ans = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)

            elif char == '+':
                ans += sign * curr
                sign = 1
                curr = 0

            elif char == '-':
                ans += sign * curr
                sign = -1
                curr = 0

            elif char == '(':
                stack.append(ans)
                stack.append(sign)
                sign = 1
                ans = 0
            
            elif char == ')':
                ans += sign * curr
                ans *= stack.pop()
                ans += stack.pop()
                curr = 0
            
        return ans + sign * curr

print(Solution().calculate("- (3 + (4 + 5))"))
