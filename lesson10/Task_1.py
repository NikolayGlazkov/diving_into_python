import math
"""
Создайте класс окружность.
📌 Класс должен принимать радиус окружности при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
class Cercle:

    def __init__(self,radius):
        self.radius = radius

    def circumference(self):
        return 2*math.pi*self.radius
    def area_circle(self):
        return math.pi * pow(self.radius,2)



c1 = Cercle(2)

print(c1.area_circle(),c1.area_circle())