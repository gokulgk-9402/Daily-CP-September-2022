from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited = set()
        minimum = len(s)
        ans = []

        def recursion(index, open, removed, string):
            if string in visited:
                return

            if index == len(s):
                nonlocal ans, minimum
                if open or removed > minimum:
                    return
                if removed < minimum:
                    minimum = removed
                    ans = []

                ans.append(string)
                return

            if s[index] == '(':
                recursion(index+1, open+1, removed, string + s[index])
                recursion(index+1, open, removed+1, string)
            elif s[index] == ')':
                if open > 0:
                    recursion(index+1,open-1,removed, string + s[index])

                recursion(index+1, open, removed +1, string)
            else:
                recursion(index +1, open, removed, string + s[index])
            visited.add(string)

        recursion(0,0,0,'')
        return ans

print(Solution().removeInvalidParentheses("()())()"))
                        