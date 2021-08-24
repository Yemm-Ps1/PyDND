class Class:
    def __init__(self, name, hit_die, level):
        self.name = name
        self.hit_die = hit_die
        self.level = level

class Rogue(Class):
    def __init__(self, level):
        super().__init__("Rogue", 8, level)