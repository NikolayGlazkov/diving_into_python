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
    
    def __add__(self, other):
        return Rectangle(self.perimeter() + other.perimeter())
    
    def __sub__(self, other):
        return Rectangle(abs(self.perimeter() - other.perimeter()))
        
    
r1 = Rectangle(12, 4)
print(r1.perimeter(), r1.square())

r2 = Rectangle(12)
print(r2.perimeter(), r2.square())

r3 = r1 + r2
r4 = r1 - r2