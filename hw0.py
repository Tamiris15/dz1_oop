class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) from {self.habitat}"

class Mammal(Animal):
    def __init__(self, name, habitat, gestation_period):
        super().__init__(name, habitat)
        self.gestation_period = gestation_period
    
    def give_birth(self):
        print(f"{self.name} gave birth after {self.gestation_period} months of gestation")
    
    def feed_milk(self):
        print(f"{self.name} is feeding milk to its young")

class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} is flying with {self.wingspan} cm wingspan")
    
    def lay_eggs(self):
        print(f"{self.name} laid eggs")

class Reptile(Animal):
    def __init__(self, name, habitat, is_cold_blooded=True):
        super().__init__(name, habitat)
        self.is_cold_blooded = is_cold_blooded
    
    def bask_in_sun(self):
        if self.is_cold_blooded:
            print(f"{self.name} is basking in the sun to warm up")
        else:
            print(f"{self.name} is enjoying the sun")

    def shed_skin(self):
        print(f"{self.name} is shedding its skin")

# Млекопитающие
class Dog(Mammal):
    def __init__(self, name, habitat="domestic", gestation_period=2, breed="unknown"):
        super().__init__(name, habitat, gestation_period)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching a stick")

class Cat(Mammal):
    def __init__(self, name, habitat="domestic", gestation_period=2, is_indoor=True):
        super().__init__(name, habitat, gestation_period)
        self.is_indoor = is_indoor
    
    def meow(self):
        print(f"{self.name} says: Meow!")
    
    def purr(self):
        print(f"{self.name} is purring")

class Horse(Mammal):
    def __init__(self, name, habitat="grasslands", gestation_period=11, speed=0):
        super().__init__(name, habitat, gestation_period)
        self.speed = speed
    
    def gallop(self):
        self.speed += 20
        print(f"{self.name} is galloping at {self.speed} km/h")
    
    def neigh(self):
        print(f"{self.name} says: Neigh!")

# Птицы
class Eagle(Bird):
    def __init__(self, name, habitat="mountains", wingspan=200):
        super().__init__(name, habitat, wingspan)
    
    def hunt(self):
        print(f"{self.name} is hunting from the sky")
    
    def screech(self):
        print(f"{self.name} emits a piercing screech")

class Penguin(Bird):
    def __init__(self, name, habitat="antarctic", wingspan=30):
        super().__init__(name, habitat, wingspan)
    
    def swim(self):
        print(f"{self.name} is swimming gracefully")
    
    def fly(self):  # Переопределяем метод fly для пингвина
        print(f"{self.name} cannot fly, but is great at swimming!")

# Рептилии
class Snake(Reptile):
    def __init__(self, name, habitat="various", is_cold_blooded=True, is_venomous=False):
        super().__init__(name, habitat, is_cold_blooded)
        self.is_venomous = is_venomous
    
    def slither(self):
        print(f"{self.name} is slithering silently")
    
    def hiss(self):
        print(f"{self.name} says: Hiss!")

class Turtle(Reptile):
    def __init__(self, name, habitat="oceans", is_cold_blooded=True, shell_color="green"):
        super().__init__(name, habitat, is_cold_blooded)
        self.shell_color = shell_color
    
    def swim(self):
        print(f"{self.name} is swimming slowly")
    
    def hide_in_shell(self):
        print(f"{self.name} hid inside its {self.shell_color} shell")

# Пример использования
if __name__ == "__main__":
    animals = [
        Dog("Rex", breed="Labrador"),
        Cat("Whiskers", is_indoor=False),
        Horse("Thunder"),
        Eagle("Sky King"),
        Penguin("Waddle"),
        Snake("Viper", is_venomous=True),
        Turtle("Speedy", shell_color="brown")
    ]
    
    for animal in animals:
        print("\n" + str(animal))
        animal.eat()
        animal.sleep()
        
        if isinstance(animal, Mammal):
            animal.give_birth()
            animal.feed_milk()
        elif isinstance(animal, Bird):
            animal.fly()
            animal.lay_eggs()
        elif isinstance(animal, Reptile):
            animal.bask_in_sun()
            animal.shed_skin()
        
        # Вызов специфичных методов
        if isinstance(animal, Dog):
            animal.bark()
            animal.fetch()
        elif isinstance(animal, Cat):
            animal.meow()
            animal.purr()
        elif isinstance(animal, Horse):
            animal.neigh()
            animal.gallop()
        elif isinstance(animal, Eagle):
            animal.hunt()
            animal.screech()
        elif isinstance(animal, Penguin):
            animal.swim()
        elif isinstance(animal, Snake):
            animal.slither()
            animal.hiss()
        elif isinstance(animal, Turtle):
            animal.swim()
            animal.hide_in_shell()
