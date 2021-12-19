# TODO: make a consolemon


class Consolemon:
    def __init__(self, name, hp, level, ftype):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = hp
        self.ftype = ftype
        self.moves = []

    def addMove(self, move):
        self.moves.append(move)
