def onajika(a, b):
    if a is b:
        return True
    else:
        return False

class Person:
    def __init__(self, name):
        self.name = name

take = Person('Kubo takefusa')
take_same = take
taki = Person('Minamino Takumi')

print(onajika(take, take_same))
print(onajika(take, taki))
