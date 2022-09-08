class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        permutation = [characters[0]]

        for char in characters[1:]:
            n = len(permutation)
            for i in range(n):
                permutation.append(permutation[i] + char)
            permutation.append(char)

        self.lst = sorted([s for s in permutation if len(s) == combinationLength])
        # print(self.lst)

    def next(self) -> str:
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        if self.lst != []:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abcdef", 3)
print(obj)
param_1 = obj.next()
print(param_1)
param_2 = obj.hasNext()
print(param_2)