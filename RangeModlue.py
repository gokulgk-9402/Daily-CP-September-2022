class RangeModule:

    def __init__(self):
        self.tracking = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.tracking, left)
        end = bisect.bisect_right(self.tracking, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
            
        self.tracking[start:end] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.tracking, left)
        end = bisect.bisect_left(self.tracking, right)
        
        return start == end and start %2 == 1
        

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.tracking, left)
        end = bisect.bisect_right(self.tracking, right)
        
        subtrack = []
        if start % 2:
            subtrack.append(left)
        if end % 2:
            subtrack.append(right)
            
        self.tracking[start:end] = subtrack
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)