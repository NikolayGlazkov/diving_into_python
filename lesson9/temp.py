# def func(a):
#     x = 42
#     res = x + a
#     return res
# x = 73
# print(func(64))

# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b
# print(add_str('Hello', 'world!')) 

from typing import Callable
def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('world!'))
print(hello('friend!'))
print(bye('wonderful world!'))
print(f'{type(add_one_str) = }, {add_one_str.__name__ = },{id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')