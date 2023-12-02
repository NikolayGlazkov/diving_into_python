# class Person:
#     max_ap = 3

#     def __init__(self,name,race = "unknown "):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level +=2
#     def change_health(self,other,quantity):
#         self.health += quantity
#         other.health -=quantity


# p1 = Person("Сильвана",'Эльф')
# p2 = Person("Иван","Человек")
# p3 = Person("Грогу")

# print(p1.health)
# p1.change_health(p2,10)
# print(p1.health)
# # p3.level_up()
# # print(p3.level)

# me_list = list((1,4,6,7))
# print(me_list)
# print(type(me_list))
# print(type(list))

# import random
# import supermodule

# result1 = random.randint(1,10)
# result2 = supermodule.randint(42)


class Person:
    max_ap = 3


    def __init__(self) -> None:
        self.level = 1
        self.health = 100
p1 = Person()
p2 = Person()
# print(f"{Person.health = }, {p1.health = }, {p2.health = }")


# print(f"{p1.health = }, {p2.health = }")

# print(f"{p1.health}")
