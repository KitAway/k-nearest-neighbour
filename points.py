import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, p: Point):
        return math.sqrt( (self.x - p.x) **2 + (self.y - p.y)**2)

    def __repr__(self):
        return "Point(x: %f, y: %f)"%(self.x, self.y)
