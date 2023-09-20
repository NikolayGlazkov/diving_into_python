import math
import decimal
# Напишите программу, которая вычисляет площадь круга и
# длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# площадь круга

decimal.getcontext().prec = 42

def circle_diameter(dim):
    return decimal.Decimal(math.pi) * pow((dim/2),2)

# длинна окруности C = 3.14 * D
def circumference (diameter):
    return decimal.Decimal(math.pi) * diameter
    
diameter = decimal.Decimal(input(f"не более тысячи :"))

print(circle_diameter(diameter))
print(circumference(diameter))
