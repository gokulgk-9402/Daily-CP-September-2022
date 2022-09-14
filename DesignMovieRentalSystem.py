from typing import List
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = []
        self.movies = defaultdict(list)
        self.prices = {}
        
        for shop, movie, price in entries:
            self.movies[movie].append((price, shop))
            self.prices[movie, shop] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies:
            return []
        
        temp = self.movies[movie][:]
        ans = []
        i = 0
        n = len(temp)
        
        while i < n and i < 5:
            m = min(temp)
            temp.remove(m)
            ans.append(m[1])
            i += 1
        
        return ans

    def rent(self, shop: int, movie: int) -> None:
        p = self.prices[movie, shop]
        self.rented.append((p, shop, movie))
        # print(self.movies[movie])
        # print(p, shop, movie)
        self.movies[movie].remove((p, shop))

    def drop(self, shop: int, movie: int) -> None:
        p = self.prices[movie, shop]
        self.rented.remove((p, shop, movie))
        self.movies[movie].append((p, shop))

    def report(self) -> List[List[int]]:
        temp = self.rented[:]
        ans = []
        i = 0
        n = len(temp)
        
        while i < n and i < 5:
            m = min(temp)
            temp.remove(m)
            ans.append([m[1], m[2]])
            i += 1
        
        return ans


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()