import math
class Circle:
    def __init__(self, r):
        self.rad = r
    def area(self):
        return(self.rad ** 2 * math.pi)

cir1 = Circle(2)
print(cir1.area())
