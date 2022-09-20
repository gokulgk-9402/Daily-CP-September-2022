#User function Template for python3

class Solution:
    def numberOfSquares(self, base):
        #code here
        n = base // 2 - 1
        return (n * (n + 1)) // 2