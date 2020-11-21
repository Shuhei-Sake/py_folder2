class Horse:
    def __init__(self, name, color, old, rider):
        self.name = name
        self.color = color
        self.old = old
        self.rider = rider

class Rider:
    def __init__(self, name, old, nationality):
        self.name = name
        self.old = old
        self.nationality = nationality

shuhei = Rider('Shuhei', 26, 'Japan')
horse1 = Horse('uma', 'black', 3, shuhei)

print(horse1.rider.name)
print(horse1.rider.old)
