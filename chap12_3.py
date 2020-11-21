class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h
        print('created')
    def area(self):
        return(self.bottom * self.height / 2)

tri1 = Triangle(4, 5)
print(tri1.area())
