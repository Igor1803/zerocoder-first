from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self): pass
    @abstractmethod
    def name(self): pass

class Sword(Weapon):
    def attack(self): return "Боец наносит удар мечом."
    def name(self): return "меч"

class Bow(Weapon):
    def attack(self): return "Боец наносит удар из лука."
    def name(self): return "лук"

class Axe(Weapon):
    def attack(self): return "Боец рубит топором!"
    def name(self): return "топор"

class Fighter:
    def __init__(self, weapon): self.weapon = weapon
    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {weapon.name()}.")
    def attack(self): return self.weapon.attack()

class Monster:
    def __init__(self, health): self.health = health
    def is_defeated(self): return self.health <= 0

def battle(fighter, monster):
    while monster.health > 0:
        print(fighter.attack())
        monster.health -= 10
        print(f"Здоровье монстра: {monster.health}")
    print("Монстр побежден!")

sword, bow, axe = Sword(), Bow(), Axe()
fighter = Fighter(sword)

battle(fighter, Monster(50))
fighter.change_weapon(bow); battle(fighter, Monster(30))
fighter.change_weapon(axe); battle(fighter, Monster(40))
