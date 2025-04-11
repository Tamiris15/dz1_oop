from abc import ABC, abstractmethod
import random

# Базовые абстрактные классы
class GameObject(ABC):
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    
    @abstractmethod
    def update(self):
        pass
    
    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y})"

class Movable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        pass

# Наследники от базовых классов
class Character(GameObject, Movable):
    def __init__(self, x, y, name, health):
        super().__init__(x, y, name)
        self.health = health
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"{self.name} moved to ({self.x}, {self.y})")
    
    def update(self):
        print(f"{self.name} updated, health: {self.health}")
    
    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, x, y, name, health, score=0):
        super().__init__(x, y, name, health)
        self.score = score
    
    def update(self):
        super().update()
        print(f"Player score: {self.score}")
    
    def collect_item(self, item):
        self.score += item.value
        print(f"Collected {item.name}, score: {self.score}")

class Enemy(Character):
    def __init__(self, x, y, name, health, damage):
        super().__init__(x, y, name, health)
        self.damage = damage
    
    def update(self):
        super().update()
        print(f"Enemy ready to attack with damage: {self.damage}")
    
    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} attacked {target.name} for {self.damage} damage")

class Boss(Enemy):
    def __init__(self, x, y, name, health, damage, special_damage):
        super().__init__(x, y, name, health, damage)
        self.special_damage = special_damage
        self.max_health = health
    
    def special_attack(self, target):
        damage = self.damage + self.special_damage
        target.health -= damage
        print(f"{self.name} used SPECIAL ATTACK on {target.name} for {damage} damage!")
    
    def heal(self):
        heal_amount = self.max_health * 0.2
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} healed for {heal_amount} health!")
    
    def summon_ally(self):
        new_enemy = Enemy(self.x + random.randint(-1, 1), 
                         self.y + random.randint(-1, 1),
                         f"{self.name}'s Minion",
                         random.randint(10, 30),
                         random.randint(5, 10))
        print(f"{self.name} summoned an ally: {new_enemy.name}")
        return new_enemy
    
    def update(self):
        super().update()
        if random.random() < 0.3:  # 30% chance to heal
            self.heal()

class Item(GameObject):
    def __init__(self, x, y, name, value):
        super().__init__(x, y, name)
        self.value = value
    
    def update(self):
        print(f"Item {self.name} waiting to be collected")

# Базовый игровой цикл
def game_loop(player, enemies, items, turns=5):
    print("\n=== GAME START ===\n")
    
    for turn in range(1, turns + 1):
        print(f"\n--- Turn {turn} ---")
        
        # Обновление всех объектов
        player.update()
        for enemy in enemies[:]:  # Копия списка для безопасного изменения
            enemy.update()
            
            # Босс может призывать союзников
            if isinstance(enemy, Boss) and random.random() < 0.25:  # 25% chance
                new_enemy = enemy.summon_ally()
                enemies.append(new_enemy)
        
        for item in items:
            item.update()
        
        # Враги атакуют игрока
        for enemy in enemies:
            if enemy.is_alive():
                if isinstance(enemy, Boss) and random.random() < 0.4:  # 40% chance for special attack
                    enemy.special_attack(player)
                else:
                    enemy.attack(player)
        
        # Проверка сбора предметов
        for item in items[:]:  # Копия списка для безопасного удаления
            if item.x == player.x and item.y == player.y:
                player.collect_item(item)
                items.remove(item)
        
        # Проверка состояния игрока
        if not player.is_alive():
            print("\nИгрок погиб! Игра окончена.")
            break
        
        # Движение игрока (для примера - случайное)
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        player.move(dx, dy)
    
    print("\n=== GAME END ===")
    print(f"Final score: {player.score}")
    print(f"Player health: {player.health}")

# 1. Создание объектов
player = Player(0, 0, "Hero", 100)
enemies = [
    Enemy(2, 3, "Goblin", 30, 5),
    Enemy(-1, 2, "Orc", 50, 8),
    Boss(5, 5, "Dragon", 150, 15, 10)
]
items = [
    Item(1, 0, "Gold Coin", 10),
    Item(0, 1, "Potion", 20),
    Item(-1, -1, "Treasure", 50)
]

# 2. Запуск игрового цикла
game_loop(player, enemies, items, turns=8)

# 4. Анализ изменения порядка наследования
"""
Если изменить порядок наследования в классе Character с (GameObject, Movable) на (Movable, GameObject), 
это повлияет на порядок разрешения методов (Method Resolution Order - MRO).

1. При текущем порядке (GameObject, Movable):
   - Python сначала ищет методы в Character, затем в GameObject, затем в Movable, затем в object.

2. При измененном порядке (Movable, GameObject):
   - Поиск будет идти: Character → Movable → GameObject → object.

В данном конкретном случае это не вызовет проблем, так как:
- Оба родительских класса не имеют пересекающихся методов (кроме __init__)
- Методы move() и update() определены в Character
- __init__ вызывается через super(), который следует MRO

Однако если бы оба родительских класса имели методы с одинаковыми именами, порядок наследования определял бы, 
какая версия метода будет использоваться.
"""
