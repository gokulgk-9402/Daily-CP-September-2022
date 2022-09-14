from typing import List
from sortedcontainers import SortedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        mem = SortedDict()
        mem.setdefault(-1, 0)

        for l, r, h in buildings:

            if r not in mem or mem.get(r) < h:
                prev = mem.bisect_right(r) - 1
                surf = mem.peekitem(prev)[-1]
                if surf < h:
                    mem[r] = surf

            if l not in mem or mem.get(l) < h:
                prev = mem.bisect_left(l) - 1
                surf = mem.peekitem(prev)[-1]
                if surf < h:
                    mem[l] = h

            start = mem.bisect_left(l)
            end = mem.bisect_left(r)

            for i in range(start, end):
                point = mem.peekitem(i)
                if point[-1] < h:
                    mem[point[0]] = h

        # print(mem)

        ans = []

        for pos in list(mem.keys())[1:]:
            height = mem.pop(pos)
            if ans and ans[-1][-1] == height:
                continue

            ans.append([pos, height])

        return ans


print(Solution().getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))