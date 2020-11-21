class Square:
    square_list = []
    def __init__(self, w):
        self.width = w
        self.square_list.append(self)
    def calculate_perimeter(self):
        return self.width * 4
    def change_size(self, cha):
        self.width = self.width + cha
    def __repr__(self):
        return '{w} by {w} by{w} by {w}'.format(w = self.width)

squ1 = Square(10)
print(squ1.calculate_perimeter())

squ1.change_size(5)
print(squ1.calculate_perimeter())

squ2 = Square(10)
squ3 = Square(29)

print(Square.square_list)
print(squ3)
