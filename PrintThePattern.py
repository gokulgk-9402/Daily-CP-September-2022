class Solution:
    def pattern(self, n):
        # code here
        last = n * (n + 1)
        ans = []
        
        def recursion(n, left, right, row):
            if n == 0:
                return

            line = "-" * row * 2
            line += "*".join(str(left + i) for i in range(n))
            line += "*"
            line += "*".join(str(right + i) for i in range(n))
            ans.append(line)

            recursion(n - 1, left + n, right - n + 1, row + 1)

        recursion(n, 1, last - n + 1, 0)
        return ans

print(Solution().pattern(3))