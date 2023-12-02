class Rectangle:
    def __init__(self, lenght, width=None):
        self.lenght = lenght
        if not width:
            self.width = lenght
        else:
            self.width = width

    def perimeter(self):
        return (self.lenght + self.width) * 2

    def square(self):
        return self.lenght * self.width


r1 = Rectangle(12, 4)
print(r1.perimeter(), r1.square())

r2 = Rectangle(12)
print(r2.perimeter(), r2.square())
