from sheet_enums import Ability

class Class:
    def __init__(self, name, hit_die, level, saving_throws: list = []):
        self.name = name
        self.hit_die = hit_die
        self.level = level
        self.saving_throws = saving_throws

class Rogue(Class):
    def __init__(self, level):
        super().__init__("Rogue", 8, level, [Ability.DEX, Ability.INT])

class Barbarian(Class):
    def __init__(self, level):
        super().__init__("Barbarian", 12, level, [Ability.STR, Ability.CON])