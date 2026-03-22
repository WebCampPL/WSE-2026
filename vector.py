import math

from point import Point

class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.point_A = Point(x1, y1)
        self.point_B = Point(x2, y2)
    def length(self) -> float:
        return math.sqrt(math.pow(self.point_B.x - self.point_A.x, 2)
                         + math.pow(self.point_B.y - self.point_A.y, 2))
