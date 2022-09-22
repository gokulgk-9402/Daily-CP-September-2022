import bisect

class SORTracker:

    def __init__(self):
        self.locations = []
        self.query_id = 0

    def add(self, name: str, score: int) -> None:
        index = bisect.bisect_left(self.locations, (-score, name))
        self.locations.insert(index, (-score, name))

    def get(self) -> str:
        self.query_id += 1
        return self.locations[self.query_id - 1][1]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()