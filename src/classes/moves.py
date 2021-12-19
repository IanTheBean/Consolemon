import random


class Move:
    def __init__(self, name, owner, damage, chance, pp):
        self.owner = owner
        self.name = name
        self.damage = damage
        self.chance = chance
        self.pp = pp

    def attack(self, consolemon):
        if random.randint(0, 100) < self.chance and self.pp <= 1:
            consolemon.hp -= self.damage
            print(self.owner.name + " has used " + self.name + "! Dealt " +
                  str(self.damage) + " damage.")
        else:
            print(self.owner.name + " has missed " + self.name + "!")
        self.pp -= 1
