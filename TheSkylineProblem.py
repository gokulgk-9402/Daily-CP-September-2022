from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ends = [x[1] for x in buildings]

        s = buildings[0][0]
        e = max(ends)


print(Solution().getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))