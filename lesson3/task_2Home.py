# Напишите функцию принимающую на вход только ключевые 
# параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

def gunc_temp(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value if hashable(value) else str(value)] = key
    return result

def hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

print(gunc_temp(a=1, b="v"))