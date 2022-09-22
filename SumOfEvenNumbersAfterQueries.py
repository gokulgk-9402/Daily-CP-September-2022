from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        curr = 0
        for num in nums:
            if num % 2 == 0:
                curr += num
        
        answer = []
        for query in queries:
            index = query[1]
            value = query[0]
            
            if nums[index] % 2 == 0:
                if value%2 == 0:
                    curr += value
                else:
                    curr -= nums[index]
            else:
                if value%2 == 1:
                    curr += nums[index] + value
                    
            nums[index] += value
            answer.append(curr)
            
        return answer