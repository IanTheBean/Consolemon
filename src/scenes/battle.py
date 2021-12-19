from ..util.ui import get_health_bar


class Battle:
    def __init__(self, player, player_pokemon, enemy_pokemon):
        self.player = player
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.width = 0

    def draw(self):
        pass

    def get_status_bar(self):
        status_bar = self.player_pokemon.name + " lvl:" + str(self.player_pokemon.level) + " " + get_health_bar(self.player_pokemon.hp, self.player_pokemon.max_hp, 10) + " vs " + get_health_bar(self.enemy_pokemon.hp,self.enemy_pokemon.max_hp, 10)  + " lvl:" + str(self.enemy_pokemon.level)  + " " + self.enemy_pokemon.name
        return status_bar
