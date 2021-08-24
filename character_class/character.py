import character_sheet as CharacterSheet



class HealthSystem():
    def __init__(self, dnd_class):
        self.hit_die = dnd_class.hit_die
        self.level = dnd_class.level

    def get_max_health(self):
        return self.hit_die * self.level

    def update_hp(self):
        pass



class Character:
    def __init__(self, name, dnd_class):
        self.name = name
        self.dnd_class = dnd_class
        self._health = HealthSystem(dnd_class)

    def print_name(self):
        print("My name is " + self.name)
    def get_max_health(self):
        return self._health.get_max_health()

class Player(Character):
    def __init__(self, name, dnd_class):
        super().__init__(name, dnd_class)


Bob = Player("Bob", CharacterSheet())
Bob.print_name()
print(Bob.get_max_health())