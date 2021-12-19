from src.classes.consolemon import Consolemon
from src.scenes.battle import Battle

squirtle = Consolemon("Squirtle", 12, 1, "water")
pikachu = Consolemon("Pikachu", 14, 2, "electric")

battle = Battle(None, squirtle, pikachu)
print(battle.get_status_bar())