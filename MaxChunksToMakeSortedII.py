from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for ele in arr:
            curr = ele
            while stack!=[] and stack[-1]>ele:
                curr = max(curr, stack.pop())
            stack.append(curr)
        return len(stack)