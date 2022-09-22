from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ctr = Counter(nums)
        v = len(nums) // 3

        ans = []

        for key in ctr:
            if ctr[key] > v:
                ans.append(key)


        return ans