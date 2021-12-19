import random

class Move:
    def __init__(self, name, damage, chance, pp):
        self.name = name
        self.damage = damage
        self.chance = chance
        self.pp = pp

    def attack(self, consolemon):
        if random.randint(0, 100) < self.chance and self.pp <= 1:
            consolemon.hp -= self.damage
        self.pp -= 1
