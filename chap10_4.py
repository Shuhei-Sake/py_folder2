import math

class Hexagon:
    def __init__(self, h):
        self.hen = h
        print('created')
    def calculate_perimeter(self):
        return ((self.hen ** 2 * math.sin(math.radians(60)) / 2) * 6)

hex1 = Hexagon(1)
print(hex1.calculate_perimeter())
