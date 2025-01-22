import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power + random.randint(-5,5) 
        damage = max(0, damage) #Урон не может быть отрицательным
        other.health -= damage
        print(f"{self.name} атаковал {other.name}, нанеся {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        player_name = input("Введите имя своего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начало битвы!")
        turn = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {turn}")
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")

            if turn % 2 != 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            turn += 1

        print("\nКонец битвы!")
        if self.player.is_alive():
            print(f"Победитель: {self.player.name}!")
        else:
            print(f"Победитель: {self.computer.name}!")

# Запуск игры
game = Game()
game.start()