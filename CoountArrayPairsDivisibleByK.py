from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        def gcd(a, b):
            if b > a:
                b, a = a, b

            if b == 0:
                return a
            
            return gcd(b, a%b)

        hashmap = defaultdict(int)

        ans = 0
        n = len(nums)

        for index, num in enumerate(nums):
            req1 = gcd(num, k)
            req2 = k // req1

            if req2 == 1:
                ans += index
            else:
                for x, y in hashmap.items():
                    if x % req2 == 0:
                        ans += y
            
            hashmap[req1] += 1

        return ans

print(Solution().countPairs(nums = [5,10,4,5,8,3], k = 8))