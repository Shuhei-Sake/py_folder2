class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def what_am_i(self):
        print('I am a shape')

class Rectangle(Shape):
    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2

class Square(Shape):
    def calculate_perimeter(self):
        return self.width * 4
    def change_size(self, cha):
        self.width = self.width + cha

rec1 = Rectangle(10, 20)
print(rec1.calculate_perimeter())

squ1 = Square(10, 10)
print(squ1.calculate_perimeter())

squ1.change_size(5)
print(squ1.calculate_perimeter())

print(rec1.what_am_i())
print(squ1.what_am_i())
