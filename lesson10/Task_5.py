class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(self.name, self.age)
        
class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        
        self.depth = depth
    
    def type_fish(self):
        if 0 < self.depth < 4:
            print('мелководные')
        elif  4 <= self.depth < 8:
            print('средневодная')
        else:
            print('глубоководная')
        
    def info(self):
        print('Это Рыбы') 
        
class Bird(Animal):
      
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        
        self.wingspan = wingspan
        
    def len_wing(self):
        return self.wingspan / 2
    
class Mammal(Animal):
    
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        
        self.weight = weight    
    
    def info(self):
        print('Это млекопитающие')
        
    def category(self):
        
        if 1 < self.weight < 10:
            print('мелкие')
        elif  10 <= self.weight < 50:
            print('средние')
        else:
            print('крупные')
            

# fish = Fish('Акула', 2, 7)
# fish.info()

# fish.type_fish()

bird = Bird('соловей', 1, 10)
bird.info()
print(bird.len_wing())

elephant = Mammal('слон', 8, 90)
elephant.info()
elephant.category()