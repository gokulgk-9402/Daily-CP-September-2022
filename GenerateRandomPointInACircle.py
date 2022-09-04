import math, random
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.cx = x_center
        self.cy = y_center

    def randPoint(self) -> List[float]:
        randRadius = self.r * math.sqrt(random.random())
        randAngle = 2 * math.pi * random.random()
        x = self.cx + randRadius * math.cos(randAngle)
        y = self.cy + randRadius * math.sin(randAngle)
        return [x, y]