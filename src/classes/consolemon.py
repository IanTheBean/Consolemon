# TODO: make a consolemon

class Consolemon:
    def __init__(self, name, hp, ftype):
        self.name = name
        self.hp = hp
        self.ftype = ftype
        self.moves = []

    def addMove(self, move):
        self.moves.append(move)
